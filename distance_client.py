import grpc
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson
import json

if __name__ == '__main__':
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DistanceServiceStub(channel)
        message = pb2.SourceDest(source_latitude=-33.0351516, source_longitude=-71.5955963,
                                 destination_latitude=-33.0348327, destination_longitude=-71.5980458)

        print(f"{MessageToJson(message)}\n")

        # call remote method
        response = stub.geodesic_distance(message)

        print("Distance:", json.loads(MessageToJson(response))["distance"])
        print("Method:", json.loads(MessageToJson(response))["method"])
        print("Distance unit:", json.loads(MessageToJson(response))["unit"])
