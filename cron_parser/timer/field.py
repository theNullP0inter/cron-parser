ANY = "*"
RANGE_IDENTIFIER="-"
LIST_IDENTIFIER=","
STEP_IDENTIFIER="/"

class Field:
    
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max
    
    def set_value(self, value):
        if value == "*":
            self.value = self._get_all_values()
            return
        
        if RANGE_IDENTIFIER in value:
            self.value = self._get_range_values(value)
            return
        
        if LIST_IDENTIFIER in value:
            self.value = self._get_list_values(value)
            return

        if STEP_IDENTIFIER in value:
            self.value = self._get_step_values(value)
            return    
    
        self.value = self._get_simple_values(value)


    def _get_simple_values(self, value):
        v = int(value)
        if v < self.min or v > self.max:
            raise Exception("Invalid value")
        return v
        
    def _get_all_values(self):
        return [x for x in range(self.min, self.max+1)]
    
    def _get_range_values(self, range_str):
        _range = range_str.split(RANGE_IDENTIFIER)
        _r0 = int(_range[0])
        _r1 = int(_range[1])

        if _r0 < self.min or _r1 < self.min or \
            _r0 > self.max or _r1 > self.max: 
            raise Exception("Invalid Range")

        return [x for x in range(_r0, _r1+1)]
    
    def _get_list_values(self, list_str):
        value_set  = set()
        for v in list_str.split(LIST_IDENTIFIER):

            if int(v) < self.min  or int(v) > self.max: 
                raise Exception("Invalid value in list")
            value_set.add(int(v))

        return list(value_set)
    
    def _get_step_values(self, step_str):
        _step = step_str.split(STEP_IDENTIFIER)
        start = _step[0]
        
        if start =="*":
            start = self.min
        else:
            start = int(start)
        
        _s1 = int(_step[1])

        if start < self.min:
            raise Exception("Invalid start for the step")
            
        values = []
        for x in range(start, self.max + 1, _s1):
            values.append(x)
        return values
    