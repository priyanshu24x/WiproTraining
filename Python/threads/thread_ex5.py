from multiprocessing import Process, Manager

def compute(n, results, index):
    """Compute the sum of squares from 0 to n-1 and store in shared list"""
    result = sum(i*i for i in range(n))
    print(f"Done computing {n}")
    results[index] = result  # store result in shared list

if __name__ == "__main__":
    numbers = [10**6, 10**7]  # numbers to compute
    manager = Manager()
    results = manager.list([0]*len(numbers))  # shared list to collect results

    processes = []
    for i, n in enumerate(numbers):
        p = Process(target=compute, args=(n, results, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Results:", list(results))