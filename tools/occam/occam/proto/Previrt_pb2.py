# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='Previrt.proto',
  package='previrt.proto',
  serialized_pb='\n\rPrevirt.proto\x12\rprevirt.proto\"\x8e\x04\n\x0bPrevirtType\x12!\n\x04type\x18\x01 \x02(\x0e\x32\x13.previrt.proto.Type\x12+\n\x03int\x18\n \x01(\n2\x1e.previrt.proto.PrevirtType.Int\x12+\n\x03vec\x18\x14 \x01(\n2\x1e.previrt.proto.PrevirtType.Vec\x12+\n\x03str\x18\x1e \x01(\n2\x1e.previrt.proto.PrevirtType.Str\x12/\n\x05\x66loat\x18( \x01(\n2 .previrt.proto.PrevirtType.Float\x12\x31\n\x06global\x18\x32 \x01(\n2!.previrt.proto.PrevirtType.Global\x1a\"\n\x03Int\x12\x0c\n\x04\x62its\x18\x02 \x02(\r\x12\r\n\x05value\x18\x03 \x01(\t\x1a\x30\n\x03Vec\x12)\n\x05\x65lems\x18\x15 \x03(\x0b\x32\x1a.previrt.proto.PrevirtType\x1a\'\n\x03Str\x12\x0c\n\x04\x64\x61ta\x18\x1f \x01(\x0c\x12\x12\n\x04\x63str\x18  \x01(\x08:\x04true\x1a\x41\n\x05\x46loat\x12*\n\x03sem\x18) \x02(\x0e\x32\x1d.previrt.proto.FloatSemantics\x12\x0c\n\x04\x64\x61ta\x18* \x01(\t\x1a/\n\x06Global\x12\x0c\n\x04name\x18\x33 \x02(\x0c\x12\x17\n\x08is_const\x18\x34 \x01(\x08:\x05\x66\x61lse\"T\n\x08\x43\x61llInfo\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x10\n\x05\x63ount\x18\x02 \x01(\r:\x01\x31\x12(\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x1a.previrt.proto.PrevirtType\"\\\n\x0b\x43\x61llRewrite\x12%\n\x04\x63\x61ll\x18\x01 \x02(\x0b\x32\x17.previrt.proto.CallInfo\x12\x14\n\x0cnew_function\x18\x02 \x02(\x0c\x12\x10\n\x04\x61rgs\x18\x03 \x03(\x05\x42\x02\x10\x01\"\xab\x01\n\x12\x43omponentInterface\x12&\n\x05\x63\x61lls\x18\x01 \x03(\x0b\x32\x17.previrt.proto.CallInfo\x12,\n\x0b\x64\x65\x66initions\x18\x02 \x03(\x0b\x32\x17.previrt.proto.CallInfo\x12+\n\x07globals\x18\x03 \x03(\x0b\x32\x1a.previrt.proto.PrevirtType\x12\x12\n\nreferences\x18\x04 \x03(\x0c\"H\n\x1b\x43omponentInterfaceTransform\x12)\n\x05\x63\x61lls\x18\x01 \x03(\x0b\x32\x1a.previrt.proto.CallRewrite\"\xcc\x03\n\nActionTree\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.previrt.proto.ActionType\x12,\n\x04\x63\x61se\x18\n \x01(\n2\x1e.previrt.proto.ActionTree.Case\x12\x32\n\x07\x66orward\x18\x14 \x01(\n2!.previrt.proto.ActionTree.Forward\x12.\n\x05\x65vent\x18\x1e \x01(\n2\x1f.previrt.proto.ActionTree.Event\x1a\x91\x01\n\x04\x43\x61se\x12\x0b\n\x03var\x18\x0b \x02(\x05\x12(\n\x04test\x18\x0c \x02(\x0b\x32\x1a.previrt.proto.PrevirtType\x12(\n\x05_then\x18\x12 \x02(\x0b\x32\x19.previrt.proto.ActionTree\x12(\n\x05_else\x18\x13 \x02(\x0b\x32\x19.previrt.proto.ActionTree\x1a\t\n\x07\x46orward\x1a\x64\n\x05\x45vent\x12\x13\n\x04\x65xit\x18\x1f \x01(\x08:\x05\x66\x61lse\x12\x0f\n\x07handler\x18  \x01(\x0c\x12\x0c\n\x04\x61rgs\x18! \x03(\x05\x12\'\n\x04then\x18\' \x01(\x0b\x32\x19.previrt.proto.ActionTree\"\x97\x01\n\x10\x45nforceInterface\x12<\n\tfunctions\x18\x01 \x03(\n2).previrt.proto.EnforceInterface.Functions\x1a\x45\n\tFunctions\x12\x0c\n\x04name\x18\x02 \x02(\x0c\x12*\n\x07\x61\x63tions\x18\x03 \x02(\x0b\x32\x19.previrt.proto.ActionTree*7\n\x04Type\x12\x05\n\x01U\x10\x00\x12\x05\n\x01I\x10\x01\x12\x05\n\x01\x46\x10\x02\x12\x05\n\x01S\x10\x03\x12\x05\n\x01V\x10\x04\x12\x05\n\x01N\x10\x05\x12\x05\n\x01G\x10\x06*\x83\x01\n\x0e\x46loatSemantics\x12\x0c\n\x08IEEEhalf\x10\x01\x12\x0e\n\nIEEEsingle\x10\x02\x12\x0e\n\nIEEEdouble\x10\x03\x12\x0c\n\x08IEEEquad\x10\x04\x12\x15\n\x11x87DoubleExtended\x10\x05\x12\t\n\x05\x42ogus\x10\x06\x12\x13\n\x0fPPCDoubleDouble\x10\x07*8\n\nActionType\x12\x08\n\x04\x43\x41SE\x10\x01\x12\x0b\n\x07\x46ORWARD\x10\x02\x12\t\n\x05\x45VENT\x10\x03\x12\x08\n\x04\x46\x41IL\x10\x04')

_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='previrt.proto.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='U', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='I', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='F', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='S', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='V', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='N', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='G', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1606,
  serialized_end=1661,
)


_FLOATSEMANTICS = descriptor.EnumDescriptor(
  name='FloatSemantics',
  full_name='previrt.proto.FloatSemantics',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='IEEEhalf', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='IEEEsingle', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='IEEEdouble', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='IEEEquad', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='x87DoubleExtended', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Bogus', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PPCDoubleDouble', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1664,
  serialized_end=1795,
)


_ACTIONTYPE = descriptor.EnumDescriptor(
  name='ActionType',
  full_name='previrt.proto.ActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CASE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FORWARD', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EVENT', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FAIL', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1797,
  serialized_end=1853,
)


U = 0
I = 1
F = 2
S = 3
V = 4
N = 5
G = 6
IEEEhalf = 1
IEEEsingle = 2
IEEEdouble = 3
IEEEquad = 4
x87DoubleExtended = 5
Bogus = 6
PPCDoubleDouble = 7
CASE = 1
FORWARD = 2
EVENT = 3
FAIL = 4



_PREVIRTTYPE_INT = descriptor.Descriptor(
  name='Int',
  full_name='previrt.proto.PrevirtType.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bits', full_name='previrt.proto.PrevirtType.Int.bits', index=0,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='previrt.proto.PrevirtType.Int.value', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=318,
  serialized_end=352,
)

_PREVIRTTYPE_VEC = descriptor.Descriptor(
  name='Vec',
  full_name='previrt.proto.PrevirtType.Vec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='elems', full_name='previrt.proto.PrevirtType.Vec.elems', index=0,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=354,
  serialized_end=402,
)

_PREVIRTTYPE_STR = descriptor.Descriptor(
  name='Str',
  full_name='previrt.proto.PrevirtType.Str',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data', full_name='previrt.proto.PrevirtType.Str.data', index=0,
      number=31, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cstr', full_name='previrt.proto.PrevirtType.Str.cstr', index=1,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=404,
  serialized_end=443,
)

_PREVIRTTYPE_FLOAT = descriptor.Descriptor(
  name='Float',
  full_name='previrt.proto.PrevirtType.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sem', full_name='previrt.proto.PrevirtType.Float.sem', index=0,
      number=41, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='previrt.proto.PrevirtType.Float.data', index=1,
      number=42, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=445,
  serialized_end=510,
)

_PREVIRTTYPE_GLOBAL = descriptor.Descriptor(
  name='Global',
  full_name='previrt.proto.PrevirtType.Global',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='previrt.proto.PrevirtType.Global.name', index=0,
      number=51, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_const', full_name='previrt.proto.PrevirtType.Global.is_const', index=1,
      number=52, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=512,
  serialized_end=559,
)

_PREVIRTTYPE = descriptor.Descriptor(
  name='PrevirtType',
  full_name='previrt.proto.PrevirtType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='previrt.proto.PrevirtType.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int', full_name='previrt.proto.PrevirtType.int', index=1,
      number=10, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vec', full_name='previrt.proto.PrevirtType.vec', index=2,
      number=20, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str', full_name='previrt.proto.PrevirtType.str', index=3,
      number=30, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='float', full_name='previrt.proto.PrevirtType.float', index=4,
      number=40, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='global', full_name='previrt.proto.PrevirtType.global', index=5,
      number=50, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PREVIRTTYPE_INT, _PREVIRTTYPE_VEC, _PREVIRTTYPE_STR, _PREVIRTTYPE_FLOAT, _PREVIRTTYPE_GLOBAL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=559,
)


_CALLINFO = descriptor.Descriptor(
  name='CallInfo',
  full_name='previrt.proto.CallInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='previrt.proto.CallInfo.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='previrt.proto.CallInfo.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='args', full_name='previrt.proto.CallInfo.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=561,
  serialized_end=645,
)


_CALLREWRITE = descriptor.Descriptor(
  name='CallRewrite',
  full_name='previrt.proto.CallRewrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='call', full_name='previrt.proto.CallRewrite.call', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_function', full_name='previrt.proto.CallRewrite.new_function', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='args', full_name='previrt.proto.CallRewrite.args', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=647,
  serialized_end=739,
)


_COMPONENTINTERFACE = descriptor.Descriptor(
  name='ComponentInterface',
  full_name='previrt.proto.ComponentInterface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='calls', full_name='previrt.proto.ComponentInterface.calls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='definitions', full_name='previrt.proto.ComponentInterface.definitions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='globals', full_name='previrt.proto.ComponentInterface.globals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='references', full_name='previrt.proto.ComponentInterface.references', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=742,
  serialized_end=913,
)


_COMPONENTINTERFACETRANSFORM = descriptor.Descriptor(
  name='ComponentInterfaceTransform',
  full_name='previrt.proto.ComponentInterfaceTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='calls', full_name='previrt.proto.ComponentInterfaceTransform.calls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=915,
  serialized_end=987,
)


_ACTIONTREE_CASE = descriptor.Descriptor(
  name='Case',
  full_name='previrt.proto.ActionTree.Case',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='var', full_name='previrt.proto.ActionTree.Case.var', index=0,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='test', full_name='previrt.proto.ActionTree.Case.test', index=1,
      number=12, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='_then', full_name='previrt.proto.ActionTree.Case._then', index=2,
      number=18, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='_else', full_name='previrt.proto.ActionTree.Case._else', index=3,
      number=19, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1192,
  serialized_end=1337,
)

_ACTIONTREE_FORWARD = descriptor.Descriptor(
  name='Forward',
  full_name='previrt.proto.ActionTree.Forward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1339,
  serialized_end=1348,
)

_ACTIONTREE_EVENT = descriptor.Descriptor(
  name='Event',
  full_name='previrt.proto.ActionTree.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exit', full_name='previrt.proto.ActionTree.Event.exit', index=0,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handler', full_name='previrt.proto.ActionTree.Event.handler', index=1,
      number=32, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='args', full_name='previrt.proto.ActionTree.Event.args', index=2,
      number=33, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='then', full_name='previrt.proto.ActionTree.Event.then', index=3,
      number=39, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1350,
  serialized_end=1450,
)

_ACTIONTREE = descriptor.Descriptor(
  name='ActionTree',
  full_name='previrt.proto.ActionTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='previrt.proto.ActionTree.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='case', full_name='previrt.proto.ActionTree.case', index=1,
      number=10, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='forward', full_name='previrt.proto.ActionTree.forward', index=2,
      number=20, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='event', full_name='previrt.proto.ActionTree.event', index=3,
      number=30, type=10, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONTREE_CASE, _ACTIONTREE_FORWARD, _ACTIONTREE_EVENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=990,
  serialized_end=1450,
)


_ENFORCEINTERFACE_FUNCTIONS = descriptor.Descriptor(
  name='Functions',
  full_name='previrt.proto.EnforceInterface.Functions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='previrt.proto.EnforceInterface.Functions.name', index=0,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='actions', full_name='previrt.proto.EnforceInterface.Functions.actions', index=1,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1535,
  serialized_end=1604,
)

_ENFORCEINTERFACE = descriptor.Descriptor(
  name='EnforceInterface',
  full_name='previrt.proto.EnforceInterface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='functions', full_name='previrt.proto.EnforceInterface.functions', index=0,
      number=1, type=10, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENFORCEINTERFACE_FUNCTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1453,
  serialized_end=1604,
)


_PREVIRTTYPE_INT.containing_type = _PREVIRTTYPE;
_PREVIRTTYPE_VEC.fields_by_name['elems'].message_type = _PREVIRTTYPE
_PREVIRTTYPE_VEC.containing_type = _PREVIRTTYPE;
_PREVIRTTYPE_STR.containing_type = _PREVIRTTYPE;
_PREVIRTTYPE_FLOAT.fields_by_name['sem'].enum_type = _FLOATSEMANTICS
_PREVIRTTYPE_FLOAT.containing_type = _PREVIRTTYPE;
_PREVIRTTYPE_GLOBAL.containing_type = _PREVIRTTYPE;
_PREVIRTTYPE.fields_by_name['type'].enum_type = _TYPE
_PREVIRTTYPE.fields_by_name['int'].message_type = _PREVIRTTYPE_INT
_PREVIRTTYPE.fields_by_name['vec'].message_type = _PREVIRTTYPE_VEC
_PREVIRTTYPE.fields_by_name['str'].message_type = _PREVIRTTYPE_STR
_PREVIRTTYPE.fields_by_name['float'].message_type = _PREVIRTTYPE_FLOAT
_PREVIRTTYPE.fields_by_name['global'].message_type = _PREVIRTTYPE_GLOBAL
_CALLINFO.fields_by_name['args'].message_type = _PREVIRTTYPE
_CALLREWRITE.fields_by_name['call'].message_type = _CALLINFO
_COMPONENTINTERFACE.fields_by_name['calls'].message_type = _CALLINFO
_COMPONENTINTERFACE.fields_by_name['definitions'].message_type = _CALLINFO
_COMPONENTINTERFACE.fields_by_name['globals'].message_type = _PREVIRTTYPE
_COMPONENTINTERFACETRANSFORM.fields_by_name['calls'].message_type = _CALLREWRITE
_ACTIONTREE_CASE.fields_by_name['test'].message_type = _PREVIRTTYPE
_ACTIONTREE_CASE.fields_by_name['_then'].message_type = _ACTIONTREE
_ACTIONTREE_CASE.fields_by_name['_else'].message_type = _ACTIONTREE
_ACTIONTREE_CASE.containing_type = _ACTIONTREE;
_ACTIONTREE_FORWARD.containing_type = _ACTIONTREE;
_ACTIONTREE_EVENT.fields_by_name['then'].message_type = _ACTIONTREE
_ACTIONTREE_EVENT.containing_type = _ACTIONTREE;
_ACTIONTREE.fields_by_name['type'].enum_type = _ACTIONTYPE
_ACTIONTREE.fields_by_name['case'].message_type = _ACTIONTREE_CASE
_ACTIONTREE.fields_by_name['forward'].message_type = _ACTIONTREE_FORWARD
_ACTIONTREE.fields_by_name['event'].message_type = _ACTIONTREE_EVENT
_ENFORCEINTERFACE_FUNCTIONS.fields_by_name['actions'].message_type = _ACTIONTREE
_ENFORCEINTERFACE_FUNCTIONS.containing_type = _ENFORCEINTERFACE;
_ENFORCEINTERFACE.fields_by_name['functions'].message_type = _ENFORCEINTERFACE_FUNCTIONS

class PrevirtType(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Int(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PREVIRTTYPE_INT
    
    # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType.Int)
  
  class Vec(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PREVIRTTYPE_VEC
    
    # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType.Vec)
  
  class Str(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PREVIRTTYPE_STR
    
    # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType.Str)
  
  class Float(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PREVIRTTYPE_FLOAT
    
    # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType.Float)
  
  class Global(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PREVIRTTYPE_GLOBAL
    
    # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType.Global)
  DESCRIPTOR = _PREVIRTTYPE
  
  # @@protoc_insertion_point(class_scope:previrt.proto.PrevirtType)

class CallInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CALLINFO
  
  # @@protoc_insertion_point(class_scope:previrt.proto.CallInfo)

class CallRewrite(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CALLREWRITE
  
  # @@protoc_insertion_point(class_scope:previrt.proto.CallRewrite)

class ComponentInterface(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPONENTINTERFACE
  
  # @@protoc_insertion_point(class_scope:previrt.proto.ComponentInterface)

class ComponentInterfaceTransform(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMPONENTINTERFACETRANSFORM
  
  # @@protoc_insertion_point(class_scope:previrt.proto.ComponentInterfaceTransform)

class ActionTree(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Case(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACTIONTREE_CASE
    
    # @@protoc_insertion_point(class_scope:previrt.proto.ActionTree.Case)
  
  class Forward(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACTIONTREE_FORWARD
    
    # @@protoc_insertion_point(class_scope:previrt.proto.ActionTree.Forward)
  
  class Event(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACTIONTREE_EVENT
    
    # @@protoc_insertion_point(class_scope:previrt.proto.ActionTree.Event)
  DESCRIPTOR = _ACTIONTREE
  
  # @@protoc_insertion_point(class_scope:previrt.proto.ActionTree)

class EnforceInterface(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Functions(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ENFORCEINTERFACE_FUNCTIONS
    
    # @@protoc_insertion_point(class_scope:previrt.proto.EnforceInterface.Functions)
  DESCRIPTOR = _ENFORCEINTERFACE
  
  # @@protoc_insertion_point(class_scope:previrt.proto.EnforceInterface)

# @@protoc_insertion_point(module_scope)