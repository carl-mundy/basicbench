import basicbench


def create_bench():
    return basicbench.Bench()


def create_experiment(*args, **kwargs):
    bench = create_bench()
    return bench.new(*args, **kwargs)
