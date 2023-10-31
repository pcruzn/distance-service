import grpc
from concurrent import futures
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from geo_location import Position
from helpers import Distance


class DistanceServicer(pb2_grpc.DistanceServiceServicer):
    def geodesic_distance(self, request, context):
        distance = Distance(
                Position(request.source_latitude, request.source_longitude, None),
                Position(request.destination_latitude, request.destination_longitude, None)
        ).km()

        response_map = {"distance": distance, "method": "geodesic", "unit": "km"}

        return pb2.Distance(**response_map)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DistanceServiceServicer_to_server(DistanceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
