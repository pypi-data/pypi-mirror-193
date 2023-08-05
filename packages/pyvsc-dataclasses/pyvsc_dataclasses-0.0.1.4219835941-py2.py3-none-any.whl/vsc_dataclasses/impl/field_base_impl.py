#****************************************************************************
# Copyright 2019-2022 Matthew Ballance and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created on May 25, 2022
#
# @author: mballance
#****************************************************************************

from .context import Context
from .context import TypeExprFieldRefKind

from .ctor import Ctor
from .expr import Expr
from .modelinfo import ModelInfo


class FieldBaseImpl(object):
    
    def __init__(self, name, typeinfo, idx):
        self._modelinfo = ModelInfo(self, name, typeinfo, idx)
        
    def _to_expr(self):
        ctor = Ctor.inst()

        if ctor.is_type_mode():
            print("FieldScalarImpl._to_expr (%s)" % self._modelinfo.name, flush=True)
            mi = self._modelinfo
            print("is_topdown_scope: %d" % mi._is_topdown_scope)
            if mi._is_topdown_scope:            
                ref = ctor.ctxt().mkTypeExprFieldRef(
                    TypeExprFieldRefKind.TopDownScope,
                    -1
                )
            else:
                ref = ctor.ctxt().mkTypeExprFieldRef(
                    TypeExprFieldRefKind.BottomUpScope,
                    -1
                )

            offset_l = []
            while mi._parent is not None:
                print("  IDX: %d" % mi._idx)
                offset_l.insert(0, mi._idx)
                print("MI: %s" % str(mi))
                mi = mi._parent
            
            for off in offset_l:
                ref.addPathElem(off)
        else:        
            print("FieldScalarImpl._to_expr (%s)" % self.model().name(), flush=True)
            ref = ctor.ctxt().mkModelExprFieldRef(self.model())
        
        return Expr(ref)
    
