import grpc
import quadratic_pb2
import quadratic_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = quadratic_pb2_grpc.QuadraticSolverStub(channel)
    coefficients = quadratic_pb2.Coefficients(a=1, b=-3, c=2)  # example coefficients
    solution = stub.SolveQuadratic(coefficients)
    print("Solution: " + solution.solution)

if __name__ == '__main__':
    run()