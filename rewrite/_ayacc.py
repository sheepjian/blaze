
# /home/stephen/continuum/pyrewrite/rewrite/_ayacc.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xe1R\r\xa5\x89\xf5\xcb\x0c\xe51\t\x94u\x16\x9e\x1f'
    
_lr_action_items = {'STRING':([0,3,9,23,24,26,27,30,39,41,],[1,1,1,1,1,1,1,1,1,1,]),'NAME':([0,3,9,23,24,26,27,30,39,41,],[12,12,12,12,12,12,12,12,12,12,]),'INT':([0,3,9,23,24,26,27,30,39,41,],[13,13,13,13,13,13,13,13,13,13,]),'DOUBLE':([0,3,9,23,24,26,27,30,39,41,],[17,17,17,17,17,17,17,17,17,17,]),'PLACEHOLDER':([5,],[20,]),']':([1,2,4,6,7,8,9,10,11,12,13,15,16,17,21,22,25,28,29,30,37,38,40,45,],[-25,-1,-5,-10,-8,-7,-28,-9,-4,-13,-12,-6,-2,-11,-20,29,-22,-27,-19,-28,-21,-16,-3,-26,]),',':([1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,],[-25,-1,-28,-5,-10,-8,-7,-28,-9,-4,-13,-12,-6,-2,-11,26,-23,-20,30,-28,-28,-22,-28,-28,-27,-19,-28,39,-17,41,-14,26,39,30,-16,-28,-3,-28,39,41,-26,]),'<':([0,3,9,23,24,26,27,30,39,41,],[5,5,5,5,5,5,5,5,5,5,]),')':([1,2,3,4,6,7,8,10,11,12,13,15,16,17,18,19,23,25,26,27,28,29,31,32,35,36,38,39,40,43,45,],[-25,-1,-28,-5,-10,-8,-7,-9,-4,-13,-12,-6,-2,-11,25,-23,-28,-22,-28,-28,-27,-19,38,-17,-24,42,-16,-28,-3,-18,-26,]),'(':([0,3,9,11,12,13,17,20,23,24,26,27,30,39,41,],[3,3,3,23,-13,-12,-11,27,3,3,3,3,3,3,3,]),'{':([0,1,3,4,6,7,8,9,10,11,12,13,15,16,17,23,25,26,27,28,29,30,38,39,45,],[-28,-25,-28,-5,-10,-8,-7,-28,-9,-4,-13,-12,-6,24,-11,-28,-22,-28,-28,-27,-19,-28,-16,-28,-26,]),'>':([20,42,],[28,45,]),'}':([1,4,6,7,8,10,11,12,13,15,17,24,25,28,29,33,34,38,41,44,45,],[-25,-5,-10,-8,-7,-9,-4,-13,-12,-6,-11,-28,-22,-27,-19,40,-14,-16,-28,-15,-26,]),'[':([0,3,9,23,24,26,27,30,39,41,],[9,9,9,9,9,9,9,9,9,9,]),'$end':([0,1,2,4,6,7,8,10,11,12,13,14,15,16,17,25,28,29,38,40,45,],[-28,-25,-1,-5,-10,-8,-7,-9,-4,-13,-12,0,-6,-2,-11,-22,-27,-19,-16,-3,-26,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tuple_value':([3,26,],[18,35,]),'term':([0,3,9,23,24,26,27,30,39,41,],[11,11,11,11,11,11,11,11,11,11,]),'string':([0,3,9,23,24,26,27,30,39,41,],[7,7,7,7,7,7,7,7,7,7,]),'avalue':([0,3,9,23,26,27,30,39,],[2,2,2,2,2,2,2,2,]),'tuple':([0,3,9,23,24,26,27,30,39,41,],[8,8,8,8,8,8,8,8,8,8,]),'expr':([0,3,9,23,26,27,30,39,],[14,19,21,32,19,32,21,32,]),'list':([0,3,9,23,24,26,27,30,39,41,],[15,15,15,15,15,15,15,15,15,15,]),'value':([0,3,9,23,24,26,27,30,39,41,],[16,16,16,16,34,16,16,16,16,34,]),'appl':([0,3,9,23,24,26,27,30,39,41,],[4,4,4,4,4,4,4,4,4,4,]),'list_value':([9,30,],[22,37,]),'placeholder':([0,3,9,23,24,26,27,30,39,41,],[10,10,10,10,10,10,10,10,10,10,]),'annotation':([24,41,],[33,44,]),'empty':([0,3,9,23,24,26,27,30,39,41,],[6,6,6,6,6,6,6,6,6,6,]),'appl_value':([23,27,39,],[31,36,43,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> avalue','expr',1,'p_expr1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',116),
  ('expr -> value','expr',1,'p_expr1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',117),
  ('avalue -> value { annotation }','avalue',4,'p_avalue','/home/stephen/continuum/pyrewrite/rewrite/parse.py',123),
  ('value -> term','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',127),
  ('value -> appl','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',128),
  ('value -> list','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',129),
  ('value -> tuple','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',130),
  ('value -> string','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',131),
  ('value -> placeholder','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',132),
  ('value -> empty','value',1,'p_value','/home/stephen/continuum/pyrewrite/rewrite/parse.py',133),
  ('term -> DOUBLE','term',1,'p_term_double','/home/stephen/continuum/pyrewrite/rewrite/parse.py',139),
  ('term -> INT','term',1,'p_term_int','/home/stephen/continuum/pyrewrite/rewrite/parse.py',143),
  ('term -> NAME','term',1,'p_term_term','/home/stephen/continuum/pyrewrite/rewrite/parse.py',147),
  ('annotation -> value','annotation',1,'p_annotation1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',155),
  ('annotation -> annotation , annotation','annotation',3,'p_annotation2','/home/stephen/continuum/pyrewrite/rewrite/parse.py',159),
  ('appl -> term ( appl_value )','appl',4,'p_appl','/home/stephen/continuum/pyrewrite/rewrite/parse.py',165),
  ('appl_value -> expr','appl_value',1,'p_appl_value1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',169),
  ('appl_value -> appl_value , appl_value','appl_value',3,'p_appl_value2','/home/stephen/continuum/pyrewrite/rewrite/parse.py',176),
  ('list -> [ list_value ]','list',3,'p_list','/home/stephen/continuum/pyrewrite/rewrite/parse.py',182),
  ('list_value -> expr','list_value',1,'p_list_value1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',186),
  ('list_value -> list_value , list_value','list_value',3,'p_list_value2','/home/stephen/continuum/pyrewrite/rewrite/parse.py',193),
  ('tuple -> ( tuple_value )','tuple',3,'p_tuple','/home/stephen/continuum/pyrewrite/rewrite/parse.py',199),
  ('tuple_value -> expr','tuple_value',1,'p_tuple_value1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',203),
  ('tuple_value -> tuple_value , tuple_value','tuple_value',3,'p_tuple_value2','/home/stephen/continuum/pyrewrite/rewrite/parse.py',210),
  ('string -> STRING','string',1,'p_string','/home/stephen/continuum/pyrewrite/rewrite/parse.py',216),
  ('placeholder -> < PLACEHOLDER ( appl_value ) >','placeholder',6,'p_placeholder1','/home/stephen/continuum/pyrewrite/rewrite/parse.py',222),
  ('placeholder -> < PLACEHOLDER >','placeholder',3,'p_placeholder2','/home/stephen/continuum/pyrewrite/rewrite/parse.py',226),
  ('empty -> <empty>','empty',0,'p_empty','/home/stephen/continuum/pyrewrite/rewrite/parse.py',232),
]