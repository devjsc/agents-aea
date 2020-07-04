# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_update.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="state_update.proto",
    package="fetch.aea.StateUpdate",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x12state_update.proto\x12\x15\x66\x65tch.aea.StateUpdate"\xc5\x0b\n\x12StateUpdateMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12M\n\x05\x61pply\x18\x05 \x01(\x0b\x32<.fetch.aea.StateUpdate.StateUpdateMessage.Apply_PerformativeH\x00\x12W\n\ninitialize\x18\x06 \x01(\x0b\x32\x41.fetch.aea.StateUpdate.StateUpdateMessage.Initialize_PerformativeH\x00\x1a\x91\x06\n\x17Initialize_Performative\x12\x89\x01\n\x1e\x65xchange_params_by_currency_id\x18\x01 \x03(\x0b\x32\x61.fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry\x12\x7f\n\x19utility_params_by_good_id\x18\x02 \x03(\x0b\x32\\.fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry\x12x\n\x15\x61mount_by_currency_id\x18\x03 \x03(\x0b\x32Y.fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry\x12x\n\x15quantities_by_good_id\x18\x04 \x03(\x0b\x32Y.fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry\x1a\x41\n\x1f\x45xchangeParamsByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a<\n\x1aUtilityParamsByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\xf4\x02\n\x12\x41pply_Performative\x12s\n\x15\x61mount_by_currency_id\x18\x01 \x03(\x0b\x32T.fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry\x12s\n\x15quantities_by_good_id\x18\x02 \x03(\x0b\x32T.fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x0e\n\x0cperformativeb\x06proto3',
)


_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY = _descriptor.Descriptor(
    name="ExchangeParamsByCurrencyIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry.value",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=887,
    serialized_end=952,
)

_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY = _descriptor.Descriptor(
    name="UtilityParamsByGoodIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry.value",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=954,
    serialized_end=1014,
)

_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY = _descriptor.Descriptor(
    name="AmountByCurrencyIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry.value",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1016,
    serialized_end=1073,
)

_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY = _descriptor.Descriptor(
    name="QuantitiesByGoodIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry.value",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1075,
    serialized_end=1132,
)

_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE = _descriptor.Descriptor(
    name="Initialize_Performative",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="exchange_params_by_currency_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.exchange_params_by_currency_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="utility_params_by_good_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.utility_params_by_good_id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="amount_by_currency_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.amount_by_currency_id",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="quantities_by_good_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.quantities_by_good_id",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY,
        _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY,
        _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
        _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=347,
    serialized_end=1132,
)

_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY = _descriptor.Descriptor(
    name="AmountByCurrencyIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry.value",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1016,
    serialized_end=1073,
)

_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY = _descriptor.Descriptor(
    name="QuantitiesByGoodIdEntry",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry.value",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1075,
    serialized_end=1132,
)

_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE = _descriptor.Descriptor(
    name="Apply_Performative",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="amount_by_currency_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.amount_by_currency_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="quantities_by_good_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.quantities_by_good_id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
        _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1135,
    serialized_end=1507,
)

_STATEUPDATEMESSAGE = _descriptor.Descriptor(
    name="StateUpdateMessage",
    full_name="fetch.aea.StateUpdate.StateUpdateMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="apply",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.apply",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="initialize",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.initialize",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE,
        _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.StateUpdate.StateUpdateMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=46,
    serialized_end=1523,
)

_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.fields_by_name[
    "exchange_params_by_currency_id"
].message_type = (
    _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.fields_by_name[
    "utility_params_by_good_id"
].message_type = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.fields_by_name[
    "amount_by_currency_id"
].message_type = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.fields_by_name[
    "quantities_by_good_id"
].message_type = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE.containing_type = _STATEUPDATEMESSAGE
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE
)
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY.containing_type = (
    _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE
)
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE.fields_by_name[
    "amount_by_currency_id"
].message_type = _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE.fields_by_name[
    "quantities_by_good_id"
].message_type = _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE.containing_type = _STATEUPDATEMESSAGE
_STATEUPDATEMESSAGE.fields_by_name[
    "apply"
].message_type = _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE
_STATEUPDATEMESSAGE.fields_by_name[
    "initialize"
].message_type = _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE
_STATEUPDATEMESSAGE.oneofs_by_name["performative"].fields.append(
    _STATEUPDATEMESSAGE.fields_by_name["apply"]
)
_STATEUPDATEMESSAGE.fields_by_name[
    "apply"
].containing_oneof = _STATEUPDATEMESSAGE.oneofs_by_name["performative"]
_STATEUPDATEMESSAGE.oneofs_by_name["performative"].fields.append(
    _STATEUPDATEMESSAGE.fields_by_name["initialize"]
)
_STATEUPDATEMESSAGE.fields_by_name[
    "initialize"
].containing_oneof = _STATEUPDATEMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["StateUpdateMessage"] = _STATEUPDATEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateUpdateMessage = _reflection.GeneratedProtocolMessageType(
    "StateUpdateMessage",
    (_message.Message,),
    {
        "Initialize_Performative": _reflection.GeneratedProtocolMessageType(
            "Initialize_Performative",
            (_message.Message,),
            {
                "ExchangeParamsByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "ExchangeParamsByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry)
                    },
                ),
                "UtilityParamsByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "UtilityParamsByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry)
                    },
                ),
                "AmountByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "AmountByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry)
                    },
                ),
                "QuantitiesByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "QuantitiesByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry)
                    },
                ),
                "DESCRIPTOR": _STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE,
                "__module__": "state_update_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Initialize_Performative)
            },
        ),
        "Apply_Performative": _reflection.GeneratedProtocolMessageType(
            "Apply_Performative",
            (_message.Message,),
            {
                "AmountByCurrencyIdEntry": _reflection.GeneratedProtocolMessageType(
                    "AmountByCurrencyIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry)
                    },
                ),
                "QuantitiesByGoodIdEntry": _reflection.GeneratedProtocolMessageType(
                    "QuantitiesByGoodIdEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY,
                        "__module__": "state_update_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry)
                    },
                ),
                "DESCRIPTOR": _STATEUPDATEMESSAGE_APPLY_PERFORMATIVE,
                "__module__": "state_update_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage.Apply_Performative)
            },
        ),
        "DESCRIPTOR": _STATEUPDATEMESSAGE,
        "__module__": "state_update_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.StateUpdate.StateUpdateMessage)
    },
)
_sym_db.RegisterMessage(StateUpdateMessage)
_sym_db.RegisterMessage(StateUpdateMessage.Initialize_Performative)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.ExchangeParamsByCurrencyIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.UtilityParamsByGoodIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.AmountByCurrencyIdEntry
)
_sym_db.RegisterMessage(
    StateUpdateMessage.Initialize_Performative.QuantitiesByGoodIdEntry
)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative.AmountByCurrencyIdEntry)
_sym_db.RegisterMessage(StateUpdateMessage.Apply_Performative.QuantitiesByGoodIdEntry)


_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._options = (
    None
)
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._options = None
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
_STATEUPDATEMESSAGE_INITIALIZE_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
_STATEUPDATEMESSAGE_APPLY_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
# @@protoc_insertion_point(module_scope)