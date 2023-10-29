from concurrent import futures
import grpc
import math
import quadratic_pb2
import quadratic_pb2_grpc

# QuadraticSolver is a class that implements the QuadraticSolver service.
class QuadraticSolver(quadratic_pb2_grpc.QuadraticSolverServicer):

    # SolveQuadratic is a method that solves a quadratic equation.
    def SolveQuadratic(self, request, context):
        a, b, c = request.a, request.b, request.c
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return quadratic_pb2.Solution(solution="No real roots")
        elif discriminant == 0:
            root = -b / (2*a)
            return quadratic_pb2.Solution(solution=f"One real root: {root}")
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return quadratic_pb2.Solution(solution=f"Two real roots: {root1}, {root2}")

# serve is a function that starts a gRPC server.
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_QuadraticSolverServicer_to_server(QuadraticSolver(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()