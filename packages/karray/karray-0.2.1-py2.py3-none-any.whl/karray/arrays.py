
import numpy as np
import pandas as pd
import csv
import json
from html import escape
from typing import List, Dict, Tuple, Union
from collections import Counter
from .utils import _format_bytes, css, union_multi_coords
from .setting import settings

class Long:
    def __init__(self, index:Dict[str, Union[np.ndarray, List[str], List[int], pd.DatetimeIndex]], value:Union[np.ndarray,List[float],List[int]]) -> None:

        # Assertion with value
        assert isinstance(value, (np.ndarray, list, float))
        if isinstance(value, np.ndarray):
            if issubclass(value.dtype.type, np.integer):
                value = value.astype(float)
            assert issubclass(value.dtype.type, float)
            if value.ndim == 0:
                value = value.reshape((value.size,))
        elif isinstance(value, float):
            value = np.array([value], dtype=float)
        else:
            value = np.array(value, dtype=float)
        assert value.ndim == 1
        # Assertion with index
        assert isinstance(index, dict)
        assert all([isinstance(index[dim], (np.ndarray,list,pd.DatetimeIndex)) for dim in index])
        dims = list(index)
        for dim in dims:
            index[dim] = _test_type_and_update(index[dim])

        assert all([index[dim].ndim == 1 for dim in index])
        assert all([index[dim].size == value.size for dim in index])
        assert 'value' not in index, "'value' can not be a dimension name as it is reserved"
        assert all([isinstance(dim, str) for dim in index])

        self._value = value
        self._index = index
        self._dims = list(self._index)

        self.rows_display = settings.rows_display
        self.decimals_display = settings.decimals_display
        self.oneshot_display = settings.oneshot_display
        self.long_nbytes = _format_bytes(sum([self._index[dim].nbytes for dim in self._index] + [self._value.nbytes]))

    def __repr__(self) -> str:
        return f'''Long
    Object size: {self.long_nbytes}
    Dimensions: {self.dims}
    Rows: {self._value.size}'''

    def _repr_html_(self) -> str:
        dims = self.dims
        items = self._value.size

        if items > self.rows_display:
            short = False
            if self.oneshot_display:
                rows = self.rows_display
            else:
                rows = int(self.rows_display/2)
        else:
            short = True
            rows = items

        columns = dims + ['value']
        html = [f"{css}"]
        html += ['<h3>[Long]</h3>',
                '<table>',
                f'<tr><th>Long object size</th><td>{self.long_nbytes}</td></tr>',
                "<!-- DENSE -->",
                f'<tr><th>Dimensions</th><td>{dims}</td></tr>',
                '<!-- SHAPE -->',
                f'<tr><th>Rows</th><td>{items}</td></tr>',
                '</table>']
        html += ["<!-- COORDS -->"]
        html += [f"<details>"]
        html += [f'<table><summary><div class="tooltip"> Show data <small>[default: 16 rows, 2 decimals]</small>']
        html += [f'<!-- A --><span class="tooltiptext tooltip-top">To change default values:<br> obj.rows_display = Int val<br>obj.decimals_display = Int val<br>obj.oneshot_display = False<!-- Z -->']
        html += ['</span></div></summary><tr><th>']
        html += [f"<th>{j}" for j in columns]
   
        for i in range(rows):
            html.append(f"<tr><th><b>{i}</b>")
            for j,v in self.items():
                val = v[i]
                html.append("<td>")
                html.append(escape(f"{val:.{self.decimals_display}f}" if issubclass(v.dtype.type, float) else f"{val}"))

        if not self.oneshot_display:
            if not short:
                html.append("<tr><th>")
                for _ in range(len(dims)+1):
                    html.append("<td>...")
                for i in range(items-rows,items,1):
                    html.append(f"<tr><th><b>{i}</b>")
                    for j,v in self.items():
                        val = v[i]
                        html.append("<td>")
                        html.append(escape(f"{val:.{self.decimals_display}f}" if issubclass(v.dtype.type, float) else f"{val}"))
        html.append("</table></details>")
        return "".join(html)

    @property
    def index(self):
        assert set(self.dims) == set(self._index.keys()), "dims names must match with index names" 
        return {dim:self._index[dim] for dim in self.dims}

    @property
    def value(self):
        return self._value.copy()

    @property
    def dims(self):
        return self._dims[:]

    @property
    def size(self):
        return self.value.size

    @property
    def ndim(self):
        return len(self.index)

    def insert(self, **kwargs):
        assert all([dim not in self.dims for dim in kwargs])
        assert all([isinstance(kwargs[dim], (str, int, dict)) for dim in kwargs])
        for dim in kwargs:
            if isinstance(kwargs[dim], dict):
                value = kwargs[dim]
                assert len(value) == 1
                existing_dim = next(iter(value))
                assert isinstance(existing_dim, str)
                assert existing_dim in self.dims
                assert isinstance(value[existing_dim], (dict, list))
                if isinstance(value[existing_dim], dict):
                    old_dim_items = list(value[existing_dim])
                    old_dim_items_set = set(old_dim_items)
                elif isinstance(value[existing_dim], list):
                    kwargs[dim][existing_dim][0] = _test_type_and_update(value[existing_dim][0])
                    old_dim_items = kwargs[dim][existing_dim][0]
                    old_dim_items_set = set(old_dim_items)
                    kwargs[dim][existing_dim][1] = _test_type_and_update(kwargs[dim][existing_dim][1])
                assert set(np.unique(self.index[existing_dim])).issubset(old_dim_items_set)
                assert len(old_dim_items) == len(old_dim_items_set) # mapping has unique keys

        index = {}
        for new_dim in kwargs:
            value = kwargs[new_dim]
            if isinstance(value, str):
                idxarray = np.empty(self.size, dtype=np.object_)
                idxarray[:] = value
            elif isinstance(value, int):
                idxarray = np.empty(self.size, dtype=np.integer)
                idxarray[:] = value
            elif isinstance(value, dict):
                existing_dim = next(iter(value))
                if isinstance(value[existing_dim], dict):
                    mapping_dict = value[existing_dim]
                    existing_dim_items = self.index[existing_dim]
                    k = np.array(list(mapping_dict)) # This must be unique
                    v = np.array(list(mapping_dict.values())) # This not necessary unique
                elif isinstance(value[existing_dim], list):
                    assert isinstance(value[existing_dim][0],np.ndarray)
                    assert isinstance(value[existing_dim][1],np.ndarray)
                    k = value[existing_dim][0]
                    v = value[existing_dim][1]
                    existing_dim_items = self.index[existing_dim]
                else:
                    raise Exception(f"type {type(value[existing_dim])} not implemented.")

                idxarray = np.array(v)[np.argsort(k)[np.searchsorted(k, existing_dim_items, sorter=np.argsort(k))]]
            index[new_dim] = idxarray

        for dim in self.index:
            index[dim] = self.index[dim]

        return Long(index=index, value=self.value)
    
    def rename(self, **kwargs):
        assert all([odim in self.dims for odim in kwargs])
        assert all([ndim not in self.dims for ndim in kwargs.values()])
        index = {}
        for dim in self.dims:
            if dim in kwargs:
                index[kwargs[dim]] = self._index[dim]
            else:
                index[dim] = self._index[dim]
        return Long(index=index, value=self._value)

    def drop(self, dims:Union[str,List[str]]):
        assert isinstance(dims, (str, list))
        index = {}
        if isinstance(dims, str):
            assert dims in self.dims
            dims = [dims]
        elif isinstance(dims, list):
            assert all([dim in self.dims for dim in dims])
        for dim in self.dims:
            if dim not in dims:
                index[dim] = self._index[dim]
        item_tuples = list(zip(*index.values()))
        if len(set(item_tuples)) == len(item_tuples):
            flag = True
        else:
            flag=False
            counts = Counter(item_tuples)
            most_common = counts.most_common(1)[0][0]
            first = item_tuples.index(most_common,0)
            second  = item_tuples.index(most_common,first+1)
            display_str = f"e.g.:\n  {tuple(index)} value\n{first} {item_tuples[first]} {self._value[first]}\n{second} {item_tuples[second]} {self._value[second]}"
        assert flag, f"Index items per row must be unique. By removing {dims} leads the existence of repeated indexes \n{display_str}\nIntead, you can use obj.reduce('{dims[0]}')\nWith an aggfunc: sum() by default"
        return Long(index=index, value=self._value)
        
    def items(self):
        dc = dict(**self.index)
        dc.update(dict(value=self._value))
        for k,v in dc.items():
            yield (k,v)

    def __getitem__(self, item):
        assert isinstance(item, (str, int, list, np.ndarray, slice, tuple))
        if isinstance(item, int):
            return Long(index={dim:self._index[dim][item] for dim in self.dims}, value=self._value[item])
        elif isinstance(item, list):
            item = np.array(item, dtype=np.integer)
            return Long(index={dim:self._index[dim][item] for dim in self.dims}, value=self._value[item])
        elif isinstance(item, np.ndarray):
            assert issubclass(item.dtype.type, np.integer) or issubclass(item.dtype.type, np.bool_)
            return Long(index={dim:self._index[dim][item] for dim in self.dims}, value=self._value[item])
        elif isinstance(item, slice):
            return Long(index={dim:self._index[dim][item] for dim in self.dims}, value=self._value[item])
        elif isinstance(item, str):
            assert item in self.dims
            return self._index[item]
        elif isinstance(item, tuple):
            assert len(item) == 2
            if isinstance(item[0], str):
                dim = item[0]
                condition = item[1]
                assert dim in self.dims
                assert isinstance(condition, (list, np.ndarray, slice))
                index_items_on_dim = self._index[dim]
                # Go over the elements of the numpy array
                if isinstance(condition, (list,np.ndarray)):
                    mask = np.isin(index_items_on_dim, condition)
                    return Long(index={dim_:self._index[dim_][mask] for dim_ in self.dims}, value=self._value[mask])
                # only works if elements of the numpy array are integers
                elif isinstance(condition, slice):
                    assert issubclass(index_items_on_dim.dtype.type, np.integer)
                    start = condition.start or int(np.min(index_items_on_dim))
                    step = condition.step or 1
                    stop = condition.stop or int(np.max(index_items_on_dim) + step)
                    arange_condition = np.arange(start,stop,step)
                    mask = np.isin(index_items_on_dim, arange_condition)
                    return Long(index={dim_:self._index[dim_][mask] for dim_ in self.dims}, value=self._value[mask])
            # Reorder dims
            elif isinstance(item[0], list):
                reorder = item[0]
                assert set(self.dims) == set(reorder)
                assert isinstance(item[1], slice)
                condition = item[1]
                start = condition.start or 0
                stop = condition.stop or self._value.size
                step = condition.step or 1
                arange_condition = np.arange(start,stop,step)
                return Long(index={dim_:self._index[dim_][arange_condition] for dim_ in reorder}, value=self._value[arange_condition])
            # TODO: Implement slice over datetime

    def __eq__(self, __o: object):
        if isinstance(__o, Long):
            dims_equal = tuple(self.dims) == tuple(__o.dims)
            if not dims_equal:
                return False
            value_equal = np.array_equal(self._value,__o._value)
            if not value_equal:
                return False
            return all(np.array_equal(self._index[dim],__o._index[dim]) for dim in self.dims)
        else:
            if np.isnan(__o):
                return np.isnan(self._value)
            elif np.isinf(__o):
                return np.isinf(self._value)
            elif isinstance(__o, (int,float)):
                return self._value == __o
            elif isinstance(__o, np.generic):
                raise Exception("np.ndarray not supported yet")
            else:
                raise Exception(f"{type(__o)} not supported yet")

    def __ne__(self, __o: object):
        if isinstance(__o, Long):
            dims_equal = tuple(self.dims) == tuple(__o.dims)
            if not dims_equal:
                return True
            value_equal = np.array_equal(self._value,__o._value)
            if not value_equal:
                return True
            return not all(np.array_equal(self._index[dim],__o._index[dim]) for dim in self.dims)
        else:
            if np.isnan(__o):
                return ~np.isnan(self._value)
            elif np.isinf(__o):
                return ~np.isinf(self._value)
            elif isinstance(__o, (int,float)):
                return self._value != __o
            elif isinstance(__o, np.generic):
                raise Exception("np.ndarray not supported yet")
            else:
                raise Exception(f"{type(__o)} not supported yet")


class Array:
    """
    A class for labelled multidimensional arrays.
    """
    def __init__(self, data:Union[Tuple[dict,Union[np.ndarray,List[float]]],Long,None]=None, coords:Union[Dict[str,Union[np.ndarray,List[str],List[int],List[np.datetime64],pd.DatetimeIndex]],None]=None):
        '''
        Initialize a karray.
        
        Args:
            data: must be a tuple of index,value or a Long object.
            coords (dict[key:str, values:list|np.ndarray[str|int|datetime64]): dictionary with all possible coordinates.

            data could be:
            - tuple index,value: index (dict[keys:str|int, values:list|np.ndarray[int|str|datetime64]): keys are dim names, values are 1d array of dim coordinates or list.
                                 value (np.ndarray|list): 1d array of float.
            - long (Long) is a Long instance
            - dense (ndarray) n-dimensional array

            A rule for the order of the array dimensions> coords keys sets dims order, otherwise index sets the order of dims. Both are subject to order list if not None.

        Example:
            >>> import karray as ka
            >>> import numpy as np
            First example
            >>> index = {'x':[2,5], 'y':[1,4]}
            >>> value = [3.0,6.0]
            >>> ar = ka.Array(data = (index, value), coords = {'x':[2,5,7], 'y':[1,4,8]}
            Second example
            >>> long = Long(index=index, value=value)
            >>> ar = ka.Array(data = long, coords = {'x':[2,5,7], 'y':[1,4,8]}
            Third example
            >>> long_format_2darray = np.array([[2,1,3.0],[5,4,6.0]]) # First two columns are dimensions, last column is value.
            >>> long = ka.numpy_to_long(array=long_format_2darray, dims=['x','y'])
            >>> ar = ka.Array(data = long, coords = {'x':[2,5,7], 'y':[1,4,8]})

        '''
        self.__dict__["_repo"] = {}
        self.long = None
        self.coords = None
        self.dense = None
        self.keep_zeros = settings.keep_zeros
        self.sort_coords = settings.sort_coords
        self.fill_missing = settings.fill_missing
        self.attr_constructor(**self.check_input(data, coords))
        return None

    def check_input(self, data, coords:dict):
        assert isinstance(data, (Long, tuple, np.ndarray, type(None)))
        if isinstance(data, Long):
            long:Union[Long,None] = data
            index:Union[dict,None] = None
            value:Union[np.ndarray,None] = None
            dense:Union[np.ndarray,None] = None
        elif isinstance(data, tuple):
            long:Union[Long,None] = None
            index:Union[dict,None] = data[0]
            value:Union[np.ndarray,None] = data[1]
            dense:Union[np.ndarray,None] = None
        elif isinstance(data, np.ndarray):
            long:Union[Long,None] = None
            index:Union[dict,None] = None
            value:Union[np.ndarray,None] = None
            dense:Union[np.ndarray,None] = data
            assert coords is not None
        else:
            long:Union[Long,None] = None
            index:Union[dict,None] = None
            value:Union[np.ndarray,None] = None
            dense:Union[np.ndarray,None] = None
            assert coords is not None
        # TODO: Add here the assertions indicated below.
        if coords is not None:
            assert isinstance(coords, dict)
            assert all([isinstance(coords[dim], (np.ndarray,list)) for dim in coords])
            cdims = list(coords)
            for dim in cdims:
                assert isinstance(dim, str)
                coords[dim] = _test_type_and_update(coords[dim])
                assert coords[dim].ndim == 1
                assert coords[dim].size == np.unique(coords[dim]).size, f"coords elements of dim '{dim}' must be unique. {coords[dim].size=}, {np.unique(coords[dim]).size=}"
            if long is not None:
                assert set(long.dims) == set(list(coords))
                assert all([set(np.unique(long.index[dim])).issubset(coords[dim]) for dim in coords])
            elif index is not None:
                assert set(list(index)) == set(list(coords))
                assert all([set(np.unique(index[dim])).issubset(coords[dim]) for dim in coords])
            elif dense is not None:
                assert dense.ndim == len(coords)
                assert dense.shape == tuple(self._shape(coords))
                assert dense.size == self._capacity(coords)
        if isinstance(data, tuple):
            assert isinstance(index, dict)
            assert all([isinstance(index[dim], (np.ndarray,list, pd.DatetimeIndex)) for dim in index])
        return dict(dense=dense, long=long, index=index, value=value, coords=coords)

    def attr_constructor(self, dense, long, index, value, coords):
        # Check input has several assertions, compare and modify accordingly
        # TODO: Noticed that coords dims could be str or int, while index in Long class can only be str. We must fix everywhere that coords keys -> dimension can only be str!
        if long is not None:
            if coords is not None: # TODO: Assertion: set(coords.keys()) == set(long.dims). Assertion long.index arrays are subset of coords values
                if len(coords) == 0:
                    assert long.ndim == 0
                    self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                    self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
                else:
                    self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                    self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
            else:
                coords = {dim:np.sort(np.unique(long.index[dim])) for dim in long.dims}
                self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
        elif index is not None: # TODO: Index is not None -> Assertion: index is a dictionary and values np.ndarray[int|str|datetime64].
            if value is None:
                raise Exception("If 'index' is not None, then 'value' must be provided. Currently 'value' is None")
            else: # TODO: assertion that values is an np.ndarray of floats
                if coords is not None: # TODO: Assertion for key and values type. Assertion: array elements must be unique. Assertion: unique elements of index must be a subset of coords elements
                    self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                    assert set(self.coords) == set(index)
                    index = {dim:index[dim] for dim in self.coords}
                    long = Long(index=index, value=value)
                    self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
                else:
                    coords = {dim:np.sort(np.unique(index[dim])) for dim in index}
                    self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                    index = {dim:index[dim] for dim in self.coords}
                    long = Long(index=index, value=value)
                    self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
        elif dense is not None:
            assert coords is not None
            if tuple(self._order_with_preference(list(coords), settings.order)) == tuple(list(coords)):
                if self.sort_coords:
                    self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                    long = self._dense_to_long(dense, coords)
                    self.dense = self._dense(long, self.coords)
                    self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
                else:
                    self.coords = coords
                    self.dense = dense
            else:
                self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                long = self._dense_to_long(dense, coords)
                self.dense = self._dense(long, self.coords)
                self.long = self._reorder_long(long, list(self.coords), self.keep_zeros)
        else:
            if value is None:
                assert value is None and index is None and coords is not None
                self.coords = self._reorder_coords(coords, settings.order, self.sort_coords)
                dtypes = {dim: self.coords[dim].dtype.type for dim in coords}
                # Create an empty Long object (It will lead to a dense array of zeros)
                if len(coords) == 0:
                    long = Long(index={}, value= np.array([], dtype=float))
                    self.long = long
                else:
                    long = Long(index={dim: np.array([], dtype=dtypes[dim]) for dim in self.coords}, value= np.array([], dtype=float))
                    self.long = long
            else:
                raise Exception("If 'value' is not None, then 'index' must be provided. Currently 'index' is None")
        return None

    def __repr__(self):
        return f"Karray.Array(data, coords)"

    def _repr_html_(self):
        html = ['<details><table><summary><div class="tooltip"> Show unique coords</div></summary>']
        html.append("<tr><th>Dimension<th>Length<th>Type<th>Items")
        for dim in self.coords:
            html.append(f"<tr><th><b>{dim}</b><td>")
            html.append(escape(f"{len(self.coords[dim])}"))
            html.append(f"<td>{self.coords[dim].dtype}<td>")
            html.append(f'<details><summary><div class="tooltip">show details</div></summary>')
            html.append(escape(f"{self.coords[dim]}"))
        html.append("</table></details>")
        dense_size = f"<tr><th>Dense object size</th><td>{_format_bytes(self.dense.nbytes)}</td></tr>"
        script = ''.join(html)
        shape = f"<tr><th>Shape</th><td>{self.shape}</td></tr>"
        
        return self.long._repr_html_().replace('[Long]','[k]array') \
                                      .replace('<!-- DENSE -->', dense_size) \
                                      .replace('<!-- COORDS -->',script) \
                                      .replace('<!-- SHAPE -->',shape) \
                                      .replace('<!-- A -->','<!-- ') \
                                      .replace('<!-- Z -->',' -->')

    def _reorder_coords(self, coords, order_preference, sort_coords):
        order = self._order_with_preference(list(coords), order_preference)
        if sort_coords:
            coords_ = {dim:np.sort(coords[dim]) for dim in order}
        else:
            coords_ = {dim:coords[dim] for dim in order}
        return coords_

    def _reorder_long(self, long, order, keep_zeros):
        long = long[order,:]
        # print(f"{keep_zeros=}")
        return long if keep_zeros else long[long != 0.0]

    def __setattr__(self, name, value):
        self._repo[name] = value

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name) # ipython requirement for repr_html
        elif name == 'long':
            if name in self._repo:
                if self._repo[name] is None:
                    assert self.dense is not None
                    self._repo[name] = self._dense_to_long(self.dense, self.coords)
                    return self._repo[name]
                else:
                    return self._repo[name]
            else:
                assert self.dense is not None
                self._repo[name] = self._dense_to_long(self.dense, self.coords)
                return self._repo[name]
        elif name == 'dense':
            if name in self._repo:
                if self._repo[name] is None:
                    assert self.long is not None
                    self._repo[name] = self._dense(self.long, self.coords)
                    return self._repo[name]
                else:
                    return self._repo[name]
            else:
                assert self.long is not None
                self._repo[name] = self._dense(self.long, self.coords)
                return self._repo[name]
        else:
            return self._repo[name]

    def _shape(self, coords):
        return [coords[dim].size for dim in coords]

    @property
    def shape(self):
        return self._shape(self.coords)

    def _capacity(self, coords):
        return int(np.prod(self._shape(coords)))

    @property
    def capacity(self):
        return self._capacity(self.coords)

    @property
    def dims(self):
        return list(self.coords)

    @property
    def dindex(self):
        arrays = np.unravel_index(np.arange(self._capacity(self.coords)), self._shape(self.coords))
        index = {dim:self.coords[dim][idx] for dim, idx in zip(self.coords, arrays)}
        return index

    def _dense(self, long, coords):
        if len(coords) == 0:
            return long.value
        long_stack = np.vstack([np.argsort(coords[dim])[np.searchsorted(coords[dim], long._index[dim], sorter=np.argsort(coords[dim]))] for dim in coords])
        shape = self._shape(coords)
        indexes = np.ravel_multi_index(long_stack, shape)
        capacity = self._capacity(coords)
        flatten_dense = np.zeros((capacity,), dtype=float)
        flatten_dense[:] = self.fill_missing
        flatten_dense[indexes] = long.value
        nd_dense = flatten_dense.view().reshape(shape)
        return nd_dense

    def _dense_to_long(self, dense, coords):
        if len(coords) == 0 and dense.ndim == 1:
            return Long(index={}, value=dense)
        arrays = np.unravel_index(np.arange(self._capacity(coords)), self._shape(coords))
        index = {dim:coords[dim][idx] for dim, idx in zip(coords, arrays)}
        long = Long(index=index, value=dense.reshape(dense.size))
        return self._reorder_long(long, list(coords), self.keep_zeros)

    @staticmethod
    def _reorder(self_long, self_coords, reorder=None):
        assert reorder is not None, "order must be provided"
        assert set(reorder) == set(self_long.dims), "order must be equal to self.dims, the order can be different, though"
        if tuple(self_long.dims) == tuple(reorder):
            return dict(data=self_long, coords=self_coords)
        coords = {k:self_coords[k] for k in reorder}
        long = self_long[reorder,:]
        return dict(data=long, coords=coords)

    def reorder(self, reorder=None):
        return Array(**self._reorder(self.long, self.coords, reorder))

    @staticmethod
    def _order_with_preference(dims:list, preferred_order:list=None):
        if preferred_order is None:
            return dims
        else:
            ordered = []
            disordered = dims[:]
            for dim in preferred_order:
                if dim in disordered:
                    ordered.append(dim)
                    disordered.remove(dim)
            ordered.extend(disordered)
            return ordered

    def _union_dims(self, other, preferred_order: list = None):
        if set(self.dims) == set(other.dims):
            return self._order_with_preference(self.dims, preferred_order)
        elif len(self.dims) == 0 or len(other.dims) == 0:
            for obj in [self,other]:
                if len(obj.dims) > 0:
                    dims = obj.dims
            return self._order_with_preference(dims, preferred_order)
        elif len(set(self.dims).symmetric_difference(set(other.dims))) > 0:
            common_dims = set(self.dims).intersection(set(other.dims))
            assert len(common_dims) > 0, "At least one dimension must be common"
            uncommon_dims = set(self.dims).symmetric_difference(set(other.dims))
            uncommon_self = [dim for dim in self.dims if dim in uncommon_dims]
            uncommon_other = [dim for dim in other.dims if dim in uncommon_dims]
            assert not all([len(uncommon_self) > 0, len(uncommon_other) > 0]), f"Uncommon dims must be in only one array. {uncommon_self=} {uncommon_other=}"
            unordered = list(set(self.dims).union(set(other.dims)))
            semi_ordered = self._order_with_preference(unordered, preferred_order)
            ordered_common = []
            if preferred_order is None:
                dims = list(common_dims) + list(uncommon_dims)
                return dims
            else:
                for dim in preferred_order:
                    if dim in common_dims:
                        ordered_common.append(dim)
                        common_dims.remove(dim)
                ordered_common.extend(common_dims)
                for dim in ordered_common:
                    if dim in semi_ordered:
                        semi_ordered.remove(dim)
                ordered =  ordered_common + semi_ordered
                return ordered

    def _union_coords(self, other, uniondims):
        coords = {}
        self_coords_bool = []
        other_coords_bool = []
        for dim in uniondims:
            if dim in self.coords:
                if dim in other.coords:
                    if self.coords[dim].size == other.coords[dim].size:
                        if all(self.coords[dim] == other.coords[dim]):
                            self_coords_bool.append(True)
                            other_coords_bool.append(True)
                            coords[dim] = self.coords[dim]
                        else:
                            coords[dim] = np.union1d(self.coords[dim], other.coords[dim])
                            if coords[dim].size == self.coords[dim].size:
                                if all(coords[dim] == self.coords[dim]):
                                    self_coords_bool.append(True)
                                else:
                                    self_coords_bool.append(False)
                            else:
                                self_coords_bool.append(False)
                            if coords[dim].size == other.coords[dim].size:
                                if all(coords[dim] == other.coords[dim]):
                                    other_coords_bool.append(True)
                                else:
                                    other_coords_bool.append(False)
                            else:
                                other_coords_bool.append(False)
                    elif set(self.coords[dim]).issubset(set(other.coords[dim])):
                        self_coords_bool.append(False)
                        other_coords_bool.append(True)
                        coords[dim] = other.coords[dim]
                    elif set(other.coords[dim]).issubset(set(self.coords[dim])):
                        self_coords_bool.append(True)
                        other_coords_bool.append(False)
                        coords[dim] = self.coords[dim]
                    else:
                        self_coords_bool.append(False)
                        other_coords_bool.append(False)
                        coords[dim] = np.union1d(self.coords[dim], other.coords[dim])
                else:
                    self_coords_bool.append(True)
                    coords[dim] = self.coords[dim]
            elif dim in other.coords:
                other_coords_bool.append(True)
                coords[dim] = other.coords[dim]
            else:
                raise Exception(f"Dimension {dim} not found in either arrays")
        self_coords_bool_ = all(self_coords_bool)
        other_coords_bool_ = all(other_coords_bool)
        return (self_coords_bool_, other_coords_bool_, coords)

    def _get_inv_dense(self, uniondims, unioncoords, coords_bool):
        self_dims = [d for d in uniondims if d in self.dims]
        if coords_bool:
            if tuple(self.dims) == tuple(self_dims):
                self_inv_dense = self.dense.T
                return self_inv_dense
        self_coords = {d:unioncoords[d] for d in self_dims}
        self_inv_dense = self._dense(self.long, self_coords).T
        return self_inv_dense

    def _pre_operation_with_array(self, other):
        uniondims = self._union_dims(other, preferred_order=settings.order)
        self_coords_bool, other_coords_bool, unioncoords = self._union_coords(other, uniondims)
        self_inv_dense = self._get_inv_dense(uniondims, unioncoords, self_coords_bool)
        other_inv_dense = other._get_inv_dense(uniondims, unioncoords, other_coords_bool)
        return self_inv_dense, other_inv_dense, unioncoords

    def _pre_operation_with_number(self):
        return self.dense.T

    def _post_operation(self, resulting_dense, coords):
        if len(coords) == 0:
            return Array(data=({},resulting_dense), coords=coords)
        return Array(data=resulting_dense.T, coords=coords)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = self_dense + other
            return self._post_operation(resulting_dense, self.coords)
        elif isinstance(other, Array):
            self_dense, other_dense, coords = self._pre_operation_with_array(other)
            resulting_dense = self_dense + other_dense
            return self._post_operation(resulting_dense, coords)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = self_dense * other
            return self._post_operation(resulting_dense, self.coords)
        elif isinstance(other, Array):
            self_dense, other_dense, coords = self._pre_operation_with_array(other)
            resulting_dense = self_dense * other_dense
            return self._post_operation(resulting_dense, coords)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = self_dense - other
            return self._post_operation(resulting_dense, self.coords)
        elif isinstance(other, Array):
            self_dense, other_dense, coords = self._pre_operation_with_array(other)
            resulting_dense = self_dense - other_dense
            return self._post_operation(resulting_dense, coords)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = self_dense / other
            return self._post_operation(resulting_dense, self.coords)
        elif isinstance(other, Array):
            self_dense, other_dense, coords = self._pre_operation_with_array(other)
            resulting_dense = self_dense/other_dense
            return self._post_operation(resulting_dense, coords)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = other + self_dense
            return self._post_operation(resulting_dense, self.coords)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = other * self_dense
            return self._post_operation(resulting_dense, self.coords)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = other - self_dense
            return self._post_operation(resulting_dense, self.coords)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            self_dense = self._pre_operation_with_number()
            resulting_dense = other / self_dense
            return self._post_operation(resulting_dense, self.coords)

    def __neg__(self):
        self_dense = self._pre_operation_with_number()
        resulting_dense = -self_dense
        return self._post_operation(resulting_dense, self.coords)

    def __pos__(self):
        self_dense = self._pre_operation_with_number()
        resulting_dense = +self_dense
        return self._post_operation(resulting_dense, self.coords)

    def items(self):
        dc = dict(**self.dindex)
        dc.update(dict(value=self.dense.reshape(-1)))
        for k,v in dc.items():
            yield (k,v)

    def to_pandas(self):
        return pd.DataFrame(dict(self.items()))

    def to_polars(self):
        import polars as pl
        return pl.from_dict(dict(self.items()))

    def to_dataframe(self, with_:str=None):
        assert with_ in ['pandas','polars']
        if with_ == "pandas":
            return self.to_pandas()
        elif with_ == "polars":
            return self.to_polars()

    def to_arrow(self):
        import pyarrow as pa
        table = pa.Table.from_pandas(pd.DataFrame({k:v for k,v in self.long.items()}))
        existing_meta = table.schema.metadata
        custom_meta_key = 'karray'
        custom_metadata = {'coords':{dim:self.coords[dim].tolist() for dim in self.coords}}
        custom_meta_json = json.dumps(custom_metadata)
        existing_meta = table.schema.metadata
        combined_meta = {custom_meta_key.encode() : custom_meta_json.encode(),**existing_meta}
        return table.replace_schema_metadata(combined_meta)

    def to_feather(self, path):
        import pyarrow.feather as ft
        table = self.to_arrow()
        ft.write_feather(table, path)
        return None

    def shrink(self, **kwargs):
        #TODO: Assertion that all elements of a list must be same type. Options are: str or int
        assert all([kw in self.coords for kw in kwargs]), "Selected dimension must be in coords"
        assert all([isinstance(kwargs[dim], (list, np.ndarray)) for dim in kwargs]), "Keeping elements must be contained in lists or np.ndarray"
        assert all([set(kwargs[kw]).issubset(self.coords[kw]) for kw in kwargs]), "All keeping elements must be included of coords"
        assert all([len(set(kwargs[kw])) == len(kwargs[kw]) for kw in kwargs]), "Keeping elements in list must be unique"
        # removing elements from coords dictionary
        new_coords = {}
        for dim in self.coords:
            if dim in kwargs:
                new_coords[dim] = _test_type_and_update(kwargs[dim])
            else:
                new_coords[dim] = self.coords[dim]
        long = self.long
        for dim in self.dims:
            if dim in kwargs:
                long = long[dim, kwargs[dim]]
        return Array(data=long, coords=new_coords)

    def add_elem(self, **kwargs):
        for dim in kwargs:
            assert dim in self.dims, f'dim: {dim} must exist in self.dims: {self.dims}'
        assert all([isinstance(kwargs[dim], (list, np.ndarray,pd.DatetimeIndex)) for dim in kwargs]), "Keeping elements must be contained in lists or np.ndarray"
        #TODO: assertion new elements of a dimension coords must have the same type of existing elements
        coords = {}
        for dim in self.coords:
            if dim in kwargs:
                coords[dim] = np.unique(np.hstack(self.coords[dim], _test_type_and_update(kwargs[dim])))
            else:
                coords[dim] = self.coords[dim]
        return Array(data=self.long, coords=coords)

    def reduce(self, dim:str, aggfunc=np.add.reduce):
        '''
        aggfunc in [np.add.reduce,np.multiply.reduce,np.average]. defult np.add.reduce
        aggfunc(np.ndarray,axis)
        axis is index of dim from self.dims.index(dim)
        '''
        assert dim in self.dims, f"dim {dim} not in self.dims: {self.dims}"
        dense = aggfunc(self.dense, axis=self.dims.index(dim))
        dims = [d for d in self.dims if d != dim]
        coords = {k:v for k,v in self.coords.items() if k in dims}
        return self._post_operation(dense.T, coords)

    def insert(self, **kwargs):
        coords = {}
        for new_dim in kwargs:
            assert new_dim not in self.dims
            value = kwargs[new_dim]
            if isinstance(value, str):
                coords[new_dim] = np.array([value], dtype=np.object_)
            elif isinstance(value, int):
                coords[new_dim] = np.array([value], dtype=np.integer)
            elif isinstance(value, dict):
                assert len(value) == 1
                existing_dim = next(iter(value))
                assert isinstance(existing_dim, str)
                assert existing_dim in self.dims
                assert isinstance(value[existing_dim], (dict,list))
                if isinstance(value[existing_dim], dict):
                    old_dim_items_set = set(value[existing_dim])
                    assert set(self.coords[existing_dim])== old_dim_items_set, f"All items in the mapping dict associated with '{new_dim}' and '{existing_dim}' must be included in .coords['{existing_dim}']"
                    assert len(value[existing_dim]) == len(old_dim_items_set), f"There are duplicate items in the mapping dict associated with '{new_dim}' and '{existing_dim}'" # mapping has unique keys
                    coords[new_dim] = np.unique(_test_type_and_update(list(value[existing_dim].values())))
                elif isinstance(value[existing_dim], list):
                    assert len(value[existing_dim]) == 2
                    old_dim_items_set = set(value[existing_dim][0])
                    assert set(self.coords[existing_dim])== old_dim_items_set, f"All items in the mapping dict associated with '{new_dim}' and '{existing_dim}' must be included in .coords['{existing_dim}']"
                    assert len(value[existing_dim][0]) == len(old_dim_items_set), f"There are duplicate items in the mapping dict associated with '{new_dim}' and '{existing_dim}'" # mapping has unique keys
                    if isinstance(value[existing_dim][0], list):
                        kwargs[new_dim][existing_dim][0] = _test_type_and_update(value[existing_dim][0])
                    assert isinstance(kwargs[new_dim][existing_dim][0], np.ndarray)
                    coords[new_dim] = np.unique(_test_type_and_update(value[existing_dim][1]))
        for dim in self.coords:
            coords[dim] = self.coords[dim]
        long = self.long.insert(**kwargs)
        return Array(data=long, coords=coords)

    def add_dim(self, **kwargs):
        return self.insert(**kwargs)
        
    def rename(self, **kwargs):
        for olddim, newdim in kwargs.items():
            assert olddim in self.dims, f"Dimension {olddim} must be in dims {self.dims}"
            assert newdim not in self.dims, f"Dimension {newdim} must not be in dims {self.dims}"
        coords = {}
        for dim, elems in self.coords.items():
            if dim in kwargs:
                coords[kwargs[dim]] = elems
            else:
                coords[dim] = elems
        return Array(data=self.dense, coords=coords)

    def drop(self, dims:Union[str, List[str]]):
        long = self.long.drop(dims=dims)
        coords = {dim:self.coords[dim] for dim in long.dims}
        return Array(data=long, coords=coords)
    
    def dropna(self):
        long = self.long
        long = long[long != np.nan]
        return Array(data=long, coords=self.coords)

    def dropinf(self, pos:bool=False, neg:bool=False):
        assert any([pos,neg]), "pos and neg cannot be both False"
        long = self.long
        if pos:
            long = long[long != np.inf]
        if neg:
            long = long[long != -np.inf]
        return Array(data=long, coords=self.coords)

    def round(self, decimals:int):
        dense = self.dense.round(decimals=decimals)
        coords = self.coords
        return Array(data=dense, coords=coords)

    def elems_to_datetime(self, new_dim:str, actual_dim:str, reference_date:str, freq:str, sort_coords:bool=True):
        assert actual_dim in self.dims
        start_date = pd.to_datetime(reference_date)
        t = pd.date_range(start=start_date, periods=self.coords[actual_dim].size, freq=freq)
        if sort_coords:
            new_array = self.insert(**{new_dim:{actual_dim:[np.sort(self.coords[actual_dim]),t]}})
        else:
            new_array = self.insert(**{new_dim:{actual_dim:[self.coords[actual_dim],t]}})
        return new_array

    def elems_to_int(self, new_dim:str, actual_dim:str):
        serie = pd.Series(data=self.coords[actual_dim])
        serie = serie.str.extract(r"(\d+)", expand=False).astype("int")
        new_array = self.insert(**{new_dim:{actual_dim:[self.coords[actual_dim], serie.values]}})
        return new_array

def _test_type_and_update(item:Union[List[str],List[int],List[np.datetime64],np.ndarray,pd.DatetimeIndex]):
    if len(item) == 0: #
        return np.array([], dtype=None) # Maybe change to np.object_
    else:
        if isinstance(item, np.ndarray):
            if issubclass(type(item[0]), str):
                if issubclass(item.dtype.type, np.object_):
                    variable_out = item.copy()
                elif issubclass(item.dtype.type, str):
                    variable_out = item.astype('object')
                else:
                    raise Exception(f"item: {item}, type: {type(item[0])} not implemented")
            elif issubclass(item.dtype.type, np.object_):
                if issubclass(type(item[0]), int):
                    variable_out = item.astype('int')
                else:
                    raise Exception(f"item: {item}, type: {type(item[0])} not implemented")
            elif issubclass(item.dtype.type, np.integer):
                variable_out = item.copy()
            elif issubclass(item.dtype.type, np.datetime64):
                variable_out = item.copy()
            elif issubclass(item.dtype.type, float):
                assert float(item[0]).is_integer(), f"item accepts float values when they are integers only. Value: {item} , type: {type(item[0])}"
                variable_out = item.astype('int')
            else:
                raise Exception(f"item: {item}, type: {type(item[0])} not implemented")
        elif isinstance(item, list):
            value_type = type(item[0])
            if issubclass(value_type, str):
                selected_type = 'object'
            elif issubclass(value_type, int):
                selected_type = 'int'
            elif issubclass(value_type, np.datetime64):
                selected_type = 'datetime64[ns]'
            elif issubclass(value_type, float):
                assert float(item[0]).is_integer(), f"item accept float values when they are integers only. Value: {item[0]} , type: {type(item[0])}"
                selected_type = 'int'
            else:
                raise Exception(f"item: {item}, type: {type(item[0])} not implemented")
            variable_out = np.array(item, dtype=selected_type)
        elif isinstance(item,pd.DatetimeIndex):
            variable_out = item.values
        else:
            raise Exception(f"item: {item}, type: {type(item)} not implemented")
        return variable_out

def concat(arrays:List[Array]):
    dims = arrays[0].dims[:]
    assert all([isinstance(arr, Array) for arr in arrays]), "All list items must be karray.array"
    assert all([set(arr.dims) == set(dims) for arr in arrays]), "All array must have the same dimensions"
    index = {dim:[] for dim in dims}
    value = []
    [index[dim].append(arr.long.index[dim]) for arr in arrays for dim in arr.dims]
    index = {dim:np.hstack(index[dim]) for dim in dims}
    [value.append(arr.long.value) for arr in arrays]
    value = np.hstack(value)
    list_of_coords = [arr.coords for arr in arrays]
    coords = union_multi_coords(*list_of_coords)
    return Array(data=(index,value), coords=coords)

def numpy_to_long(array:np.ndarray, dims:list) -> Long:
    assert isinstance(array, np.ndarray)
    assert isinstance(dims, list)
    assert array.ndim == 2, "Array must be a 2 dimensions array"
    assert len(dims) + 1 == len(array.T), f"Numpy array must contain {len(dims) + 1} columns"
    value = array.T[len(dims)]
    _index = {dim:arr for dim, arr in zip(dims, array.T[0:len(dims)])}
    _value = value if issubclass(value.dtype.type, float) else value.astype(float)
    return Long(_index, _value)

def _pandas_to_array(df, coords:Union[dict,None]=None):
    assert "value" in df.columns, "Column named 'value' must exist"
    value = df["value"].values
    df = df.drop(labels="value", axis=1)
    index = df.to_dict(orient='list')
    return dict(data=(index,value), coords=coords)

def from_pandas(df, coords:Union[dict,None]=None):
    return Array(**_pandas_to_array(df, coords=coords))

def _polars_to_array(df, coords:Union[dict,None]=None):
    assert "value" in df.columns, "Column named 'value' must exist"
    value = df["value"].to_numpy()
    df = df.drop(columns="value")
    index = df.to_dict(as_series=False)
    return dict(data=(index,value), coords=coords)

def from_polars(df, coords:Union[dict,None]=None):
    return Array(**_polars_to_array(df, coords=coords))

def _from_feather(path, use_threads=True, with_:str=None):
    assert with_ in ["pandas","polars"]
    import pyarrow.feather as ft
    restored_table = ft.read_table(path, use_threads=use_threads)
    column_names = restored_table.column_names
    assert "value" in column_names, "Column named 'value' must exist"
    custom_meta_key = 'karray'
    if custom_meta_key.encode() in restored_table.schema.metadata:
        restored_meta_json = restored_table.schema.metadata[custom_meta_key.encode()]
        restored_meta = json.loads(restored_meta_json)
        assert "coords" in restored_meta
        if with_ == "pandas":
            return _pandas_to_array(df=restored_table.to_pandas(), coords=restored_meta['coords'])
        elif with_ == "polars":
            import polars as pl
            return _polars_to_array(df=pl.from_arrow(restored_table), coords=restored_meta['coords'])
    else:
        #TODO: logger: karray not present in restored_table.schema.metadata
        if with_ == "pandas":
            return _pandas_to_array(df=restored_table.to_pandas(), coords=None)
        elif with_ == "polars":
            import polars as pl
            return _polars_to_array(df=pl.from_arrow(restored_table), coords=None)

def from_feather(path, use_threads=True, with_:str="polars"):
    return Array(**_from_feather(path=path, use_threads=use_threads, with_=with_))

def _from_csv(path, coords:Union[dict,None]=None, delimiter:str=',', with_:str="numpy"):
    assert with_ in ["numpy","pandas","polars"]
    if with_ == "numpy":
        with open(path,'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                file_load_headers = row
                break
        assert file_load_headers[-1] == "value", f"{file_load_headers[-1]}"
        if coords is None:
            dims = file_load_headers[:-1] # remove last column ('value')
        else:
            dims = list(coords)
        
        raw_csv =  np.loadtxt(path, delimiter=delimiter, skiprows=1, dtype=np.object_)

        index = {}
        i = 0
        for dim in dims:
            arr = raw_csv[:,i]
            arr_ = np.array(list(arr))
            if not issubclass(arr_.dtype.type, str):
                arr = arr_
            index[dim] = arr
            i+=1
        if dims:
            value = raw_csv[:,i].astype(float)
        else:
            assert raw_csv.ndim == 0
            value = raw_csv.astype(float)
        return dict(data=(index,value), coords=coords)
    elif with_ == "pandas":
        df = pd.read_csv(path)
        return _pandas_to_array(df=df, coords=coords)
    elif with_ == "polars":
        import polars as pl
        df = pl.read_csv(path)
        return _polars_to_array(df=df, coords=coords)

def from_csv(path, coords:Union[dict,None]=None, delimiter:str=',', with_:str="numpy"):
    return Array(**_from_csv(path, coords=coords, delimiter=delimiter, with_=with_))
