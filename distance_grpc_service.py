import grpc
from concurrent import futures
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from geo_location import Position
from helpers import Distance


class DistanceServicer(pb2_grpc.DistanceServiceServicer):
    def geodesic_distance(self, request, context):
        if request.unit == "km":
            distance = Distance(
                    Position(request.source.latitude, request.source.longitude, request.source.altitude),
                    Position(request.destination.latitude, request.destination.longitude, request.destination.altitude)
            ).km()
        if request.unit == "nm":
            distance = Distance(
                Position(request.source.latitude, request.source.longitude, request.source.altitude),
                Position(request.destination.latitude, request.destination.longitude, request.destination.altitude)
            ).nautical()

        response_map = {"distance": distance, "method": "geodesic", "unit": str(request.unit)}

        return pb2.Distance(**response_map)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DistanceServiceServicer_to_server(DistanceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
