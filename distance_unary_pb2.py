# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: distance_unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64istance_unary.proto\"|\n\nSourceDest\x12\x17\n\x0fsource_latitude\x18\x01 \x01(\x02\x12\x18\n\x10source_longitude\x18\x02 \x01(\x02\x12\x1c\n\x14\x64\x65stination_latitude\x18\x03 \x01(\x02\x12\x1d\n\x15\x64\x65stination_longitude\x18\x04 \x01(\x02\":\n\x08\x44istance\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t2@\n\x0f\x44istanceService\x12-\n\x11geodesic_distance\x12\x0b.SourceDest\x1a\t.Distance\"\x00\x62\x06proto3')



_SOURCEDEST = DESCRIPTOR.message_types_by_name['SourceDest']
_DISTANCE = DESCRIPTOR.message_types_by_name['Distance']
SourceDest = _reflection.GeneratedProtocolMessageType('SourceDest', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEDEST,
  '__module__' : 'distance_unary_pb2'
  # @@protoc_insertion_point(class_scope:SourceDest)
  })
_sym_db.RegisterMessage(SourceDest)

Distance = _reflection.GeneratedProtocolMessageType('Distance', (_message.Message,), {
  'DESCRIPTOR' : _DISTANCE,
  '__module__' : 'distance_unary_pb2'
  # @@protoc_insertion_point(class_scope:Distance)
  })
_sym_db.RegisterMessage(Distance)

_DISTANCESERVICE = DESCRIPTOR.services_by_name['DistanceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOURCEDEST._serialized_start=24
  _SOURCEDEST._serialized_end=148
  _DISTANCE._serialized_start=150
  _DISTANCE._serialized_end=208
  _DISTANCESERVICE._serialized_start=210
  _DISTANCESERVICE._serialized_end=274
# @@protoc_insertion_point(module_scope)
