from utils import Countries,Country
from mst_tsp import MstTsp
from dp_tsp import DpTsp
import time



def main():
    countries = Countries()
    countries.parse_json_countries(44)

    # countries.parse_json_by_region("Northern Europe")
    # countries.parse_json_by_region("Eastern Europe")
    # countries.parse_json_by_region("Southern Europe")
    # countries.parse_json_by_region("Western Europe")

    adj_matrix = countries.get_adj_matrix()

    # Start timing for MST TSP
    start_time_mst = time.time()
    start_time_alter = time.time()
    mst_tsp = MstTsp(adj_matrix)
    path_mst = mst_tsp.calculate_tsp(adj_matrix)
    end_time_mst = time.time()
    cost_mst = (int)(mst_tsp.calculate_tsp_cost(path_mst, adj_matrix))
    elapsed_time_mst = (end_time_mst - start_time_mst) * 1000


    # alter_mst adalah minimum spanning tree ditambah 2-Opt
    alter_mst = mst_tsp.alter_tour(path_mst, cost_mst)
    alter_cost = (int)(mst_tsp.calculate_tsp_cost(alter_mst, adj_matrix))
    end_time_alter = time.time()

    # Start timing for DP TSP

    # Uncomment code below if you want to test TSP for (n < 20)
    # Fpr n > 20, it will take a long time to compute


    # start_time_dp = time.time()
    # dp_tsp = DpTsp(adj_matrix)
    # path_dp = dp_tsp.solve()
    # end_time_dp = time.time()
    # cost_dp = (int)(dp_tsp.get_cost())
    # elapsed_time_dp = (end_time_dp - start_time_dp) * 1000
    # countries.plot_lines(path_dp)

    # print("DP TSP path:", path_dp)
    # print("DP TSP cost:", cost_dp) 
    # print("DP TSP elapsed time:", elapsed_time_dp, "ms")

    print("MST TSP path:", path_mst)
    print("MST TSP cost:", cost_mst)
    print("MST TSP elapsed time:", elapsed_time_mst, "ms")


    # print("Altered path:", alter_mst)
    print("TSP Using Minimum Spanning Tree and 2-Opt")
    countries.print_countries_path(alter_mst)
    print("\nTour cost:", alter_cost)
    print("Execution time:", (end_time_alter - start_time_alter) * 1000, "ms")
    countries.plot_lines(alter_mst)



    # print("Ratio : " , cost_mst/cost_dp)

main()
