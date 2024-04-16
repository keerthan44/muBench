# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mub_pb2 as mub__pb2


class MicroServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMicroServiceResponse = channel.unary_unary(
                '/microservice.MicroService/GetMicroServiceResponse',
                request_serializer=mub__pb2.Message.SerializeToString,
                response_deserializer=mub__pb2.MessageResponse.FromString,
                )


class MicroServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMicroServiceResponse(self, request, context):
        """A simple RPC.

        Obtains the MessageResponse at a given position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MicroServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMicroServiceResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMicroServiceResponse,
                    request_deserializer=mub__pb2.Message.FromString,
                    response_serializer=mub__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'microservice.MicroService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MicroService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMicroServiceResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/microservice.MicroService/GetMicroServiceResponse',
            mub__pb2.Message.SerializeToString,
            mub__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
