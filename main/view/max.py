import base64
from io import BytesIO
import matplotlib.pyplot as plt
import math
import pandas as pd
import mysql.connector


def loaddata_max3(fac_number, fflow, hhead,dfmax):
    import numpy as np
    im_size_lst = dfmax.query(f"data_type == 'QH' and fac_number == '{fac_number}'")[
        'imp_dia'].unique().tolist()
    imp_x_list = []
    imp_y_list = []
    # print(im_size_lst,"5484548")
    for imp_dia in im_size_lst:
        flows = dfmax.query(f"data_type == 'QH' and imp_dia == {imp_dia}and fac_number == '{fac_number}'")[
            'flow'].tolist()
        imp_x_list.append(flows)

        heads = dfmax.query(f"data_type == 'QH' and imp_dia == {imp_dia}and fac_number == '{fac_number}'")[
            'head'].tolist()
        imp_y_list.append(heads)
    # print(im_size_lst)
    
    (
        imp_x_1,
        imp_x_2,
        imp_x_3,
        imp_x_4,
        imp_x_5,
        imp_x_6,
        imp_x_7,
        imp_x_8,
        imp_x_9,
    ) = imp_x_list + [[0]] * (9 - len(im_size_lst))
        
    (
        imp_y_1,
        imp_y_2,
        imp_y_3,
        imp_y_4,
        imp_y_5,
        imp_y_6,
        imp_y_7,
        imp_y_8,
        imp_y_9,
    ) = imp_y_list + [[0]] * (9 - len(im_size_lst))
        
        # Impeller
    imp_data_x = [
        imp_x_1,
        imp_x_2,
        imp_x_3,
        imp_x_4,
        imp_x_5,
        imp_x_6,
        imp_x_7,
        imp_x_8,
        imp_x_9,
    ]
    imp_data_y = [
        imp_y_1,
        imp_y_2,
        imp_y_3,
        imp_y_4,
        imp_y_5,
        imp_y_6,
        imp_y_7,
        imp_y_8,
        imp_y_9,
    ]
    
    # -------- Poly Method ----------
    max_lmpeller = max(im_size_lst)
    min_lmpeller = min(im_size_lst)
    # print('max_lmpeller',max_lmpeller)
    # print('min_lmpeller',min_lmpeller)
    imp_x_top = dfmax.query(
        f"data_type == 'QH' and imp_dia == {max_lmpeller} and fac_number == '{fac_number}'"
    )["flow"].tolist()
    imp_y_top =  dfmax.query(
        f"data_type == 'QH' and imp_dia == {max_lmpeller} and fac_number == '{fac_number}'"
    )["head"].tolist()
    imp_x_botton = dfmax.query(
        f"data_type == 'QH' and imp_dia == {min_lmpeller} and fac_number == '{fac_number}'"
    )["flow"].tolist()
    imp_y_botton = dfmax.query(
        f"data_type == 'QH' and imp_dia == {min_lmpeller} and fac_number == '{fac_number}'"
    )["head"].tolist()

    # print("flow",imp_x_top)
    # print("head",imp_y_top)

    imp_x_center_top = max(imp_x_top)
    imp_y_center_top = min(imp_y_top)

    # print("imp_x_center_top",imp_x_center_top)
    # print("imp_y_center_top",imp_y_center_top)

    imp_x_center_botton = max(imp_x_botton)
    imp_y_center_botton = min(imp_y_botton)

    center_data_x = ([imp_x_center_top,imp_x_center_botton])
    # print('x',center_data_x)
    center_data_y = ([imp_y_center_top,imp_y_center_botton])
    # print('y',center_data_y)
    degree = 1  # Specify the degree of the polynomial
    # print(len(imp_x_top))
    # print(len(imp_y_top))
    coefficients_top = np.polyfit(imp_x_top, imp_y_top, degree)
    coefficients_botton = np.polyfit(imp_x_botton, imp_y_botton, degree)
    coefficients_center = np.polyfit(center_data_x, center_data_y,1)


    # Calculate the y-coordinate for x = 5
    equation_top_func = np.poly1d(coefficients_top)
    equation_botton_func = np.poly1d(coefficients_botton)
    equation_center_func = np.poly1d(coefficients_center)

    # inputsection
    flow_input = float(fflow)  # รอรับจากลูกค้า
    Head_input = float(hhead)  # รอรับจากลูกค้า

    x_value = flow_input
    y_value_top = float(format(equation_top_func(x_value),'.2f'))
    y_value_botton = float(format(equation_botton_func(x_value),'.2f'))
    y_value_center = float(format(equation_center_func(x_value),'.2f'))

    # print(f"TOP For x = {x_value}, y = {y_value_top}")
    # # print(f"BOT For x = {x_value}, y = {y_value_botton}")
    # print(f"CEN For x = {x_value}, y = {y_value_center}")
    ###########################################
    ###########################################
    ### kw


    kw_size_lst = dfmax.query(f"data_type == 'KW' and fac_number == '{fac_number}'")[
        'imp_dia'].unique().tolist()

    power_x_list = []
    power_y_list = []

    for kw_dia in kw_size_lst:
        flow_p = dfmax.query(
            f"data_type =='KW' and imp_dia =={kw_dia}and fac_number == '{fac_number}'")['flow'].tolist()
        power_x_list.append(flow_p)

        power = dfmax.query(
            f"data_type =='KW' and imp_dia =={kw_dia}and fac_number == '{fac_number}'")['kw'].tolist()
        power_y_list.append(power)

    (
        power_x_1,
        power_x_2,
        power_x_3,
        power_x_4,
        power_x_5,
        power_x_6,
        power_x_7,
        power_x_8,
        power_x_9,
    ) = power_x_list + [[0]] * (9 - len(kw_size_lst))
    # print(power_1)
    (
        power_y_1,
        power_y_2,
        power_y_3,
        power_y_4,
        power_y_5,
        power_y_6,
        power_y_7,
        power_y_8,
        power_y_9,
    ) = power_y_list + [[0]] * (9 - len(kw_size_lst))
    # print(flow_p_1)

    ###power
    power_data_x = [
        power_x_1,
        power_x_2,
        power_x_3,
        power_x_4,
        power_x_5,
        power_x_6,
        power_x_7,
        power_x_8,
        power_x_9,
    ]
    power_data_y = [
        power_y_1,
        power_y_2,
        power_y_3,
        power_y_4,
        power_y_5,
        power_y_6,
        power_y_7,
        power_y_8,
        power_y_9,
    ]

    #####################################
    ###npshr

    npshr_x_list = []
    npshr_y_list = []
    npshr_size_lst = (
        dfmax.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")[
            "npshr"
        ]
        .unique()
        .tolist()
    )
    for npshr in npshr_size_lst:
        npshr_x_ = dfmax.query(f"data_type =='NPSHR'and fac_number == '{fac_number}'and npshr == {npshr}")['flow'].tolist()
        npshr_x_list.append(npshr_x_)

        npshr_y_ = dfmax.query(f"data_type =='NPSHR' and fac_number == '{fac_number}'and npshr == {npshr}")['head'].tolist()
        npshr_y_list.append(npshr_y_)


    (
    npshr_x_1,
            npshr_x_2,
            npshr_x_3,
            npshr_x_4,
            npshr_x_5,
            npshr_x_6,
            npshr_x_7,
            npshr_x_8,
            npshr_x_9,
        ) = npshr_x_list + [[0]] * (9 - len(npshr_size_lst))
    
    (npshr_y_1,
        npshr_y_2,
        npshr_y_3,
        npshr_y_4,
        npshr_y_5,
        npshr_y_6,
        npshr_y_7,
        npshr_y_8,
        npshr_y_9,) = npshr_y_list + [[0]] * (9 - len(npshr_size_lst))

    ##npshr
    npshr_data_x = [
        npshr_x_1,
        npshr_x_2,
        npshr_x_3,
        npshr_x_4,
        npshr_x_5,
        npshr_x_6,
        npshr_x_7,
        npshr_x_8,
        npshr_x_9,
    ]
    npshr_data_y = [
        npshr_y_1,
        npshr_y_2,
        npshr_y_3,
        npshr_y_4,
        npshr_y_5,
        npshr_y_6,
        npshr_y_7,
        npshr_y_8,
        npshr_y_9,
    ]

    ##################################
    # effS
    eff_x_list = []
    eff_y_list = []
    eff_size_lst = (
        dfmax.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")["eff"]
        .unique()
        .tolist()
    )

    for eff_size in eff_size_lst:
        eff_flow = (
            dfmax.query(
                f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["flow"]
            .tolist()
        )

        eff_x_list.append(eff_flow)

        # eff_flow_list.sort()
        eff_head = (
            dfmax.query(
                f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["head"]
            .tolist()
        )
        eff_y_list.append(eff_head)

    (
        eff_x_1,
        eff_x_2,
        eff_x_3,
        eff_x_4,
        eff_x_5,
        eff_x_6,
        eff_x_7,
        eff_x_8,
        eff_x_9,
    ) = eff_x_list + [[0]] * (9 - len(eff_size_lst))

    (
        eff_y_1,
        eff_y_2,
        eff_y_3,
        eff_y_4,
        eff_y_5,
        eff_y_6,
        eff_y_7,
        eff_y_8,
        eff_y_9,
    ) = eff_y_list + [[0]] * (9 - len(eff_size_lst))

    ###eff
    eff_data_x = [
        eff_x_1,
        eff_x_2,
        eff_x_3,
        eff_x_4,
        eff_x_5,
        eff_x_6,
        eff_x_7,
        eff_x_8,
        eff_x_9,
    ]
    eff_data_y = [
        eff_y_1,
        eff_y_2,
        eff_y_3,
        eff_y_4,
        eff_y_5,
        eff_y_6,
        eff_y_7,
        eff_y_8,
        eff_y_9,
    ]
   # ---------------------- Eff Plot Chart -------------------------------
    eff_x_list_plot = []
    eff_y_list_plot = []
    eff_size_lst_plot = (
        dfmax.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"]
        .unique()
        .tolist()
    )
    eff_size_lst_plot = sorted(eff_size_lst_plot)
    rightSelcet = 0
    # print('eff_size_lst_plot',eff_size_lst_plot)
    selected_indices = [i for i, item in enumerate(eff_size_lst_plot) if 'R' in item]
    for index in selected_indices:
        rightSelcet = index
        break


    for eff_size_plot in eff_size_lst_plot:
        eff_flow_plot = (
            dfmax.query(
                f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["flow"]
            .tolist()
        )

        # print("Flow :",eff_flow)
        eff_x_list_plot.append(eff_flow_plot)

        # eff_flow_list.sort()
        eff_head_plot = (
            dfmax.query(
                f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["head"]
            .tolist()
        )
        eff_y_list_plot.append(eff_head_plot)
        
    # print(eff_y_list_plot)
    (
        eff_x_1_plot,
        eff_x_2_plot,
        eff_x_3_plot,
        eff_x_4_plot,
        eff_x_5_plot,
        eff_x_6_plot,
        eff_x_7_plot,
        eff_x_8_plot,
        eff_x_9_plot,
        eff_x_10_plot,
        eff_x_11_plot,
        eff_x_12_plot,
        eff_x_13_plot,
        eff_x_14_plot,
        eff_x_15_plot,
    ) = eff_x_list_plot + [[0]] * (15 - len(eff_size_lst_plot))

    (
        eff_y_1_plot,
        eff_y_2_plot,
        eff_y_3_plot,
        eff_y_4_plot,
        eff_y_5_plot,
        eff_y_6_plot,
        eff_y_7_plot,
        eff_y_8_plot,
        eff_y_9_plot,
        eff_y_10_plot,
        eff_y_11_plot,
        eff_y_12_plot,
        eff_y_13_plot,
        eff_y_14_plot,
        eff_y_15_plot,
    ) = eff_y_list_plot + [[0]] * (15 - len(eff_size_lst_plot))
    "----------------------------------------------------------------------"

    # inputsection

    flow_input = float(fflow)  # รอรับจากลูกค้า
    Head_input = float(hhead)  # รอรับจากลูกค้า
    x_max = float(
        (
            max(
                [
                    max(imp_x_1),
                    max(imp_x_2),
                    max(imp_x_3),
                    max(imp_x_4),
                    max(imp_x_5),
                    max(imp_x_6),
                    max(imp_x_7),
                    max(imp_x_8),
                    max(imp_x_9),
                ]
            )
        )
    )
    x_min = float(
        (
            min(
                [
                    min(imp_x_1),
                    min(imp_x_2),
                    min(imp_x_3),
                    min(imp_x_4),
                    min(imp_x_5),
                    min(imp_x_6),
                    min(imp_x_7),
                    min(imp_x_8),
                    min(imp_x_9),
                ]
            )
        )
    )
    y_max = float(
        (
            max(
                [
                    max(imp_y_1),
                    max(imp_y_2),
                    max(imp_y_3),
                    max(imp_y_4),
                    max(imp_y_5),
                    max(imp_y_6),
                    max(imp_y_7),
                    max(imp_y_8),
                    max(imp_y_9),
                ]
            )
        )
    )
    y_min = float(
        (
            min(
                [
                    min(imp_y_1),
                    min(imp_y_2),
                    min(imp_y_3),
                    min(imp_y_4),
                    min(imp_y_5),
                    min(imp_y_6),
                    min(imp_y_7),
                    min(imp_y_8),
                    min(imp_y_9),
                ]
            )
        )
    )

    # print(fac_number)
    '----------------------------------------------------------------------'
    # print(flow_p)
    # print(flow_power)
    # print(head_power)
    # inputsection
    if rightSelcet is None:
        rightSelcet = len(eff_size_lst)-1

    # print('eff_size_lst_plot_sort',eff_size_lst_plot)
    # print('eff_size_lst_plot',eff_size_lst_plot[0])
    # print('eff_size_lst_plot',eff_size_lst_plot[rightSelcet])
    flow_input = float(fflow)  # รอรับจากลูกค้า
    Head_input = float(hhead)  # รอรับจากลูกค้า

    coefficients_eff_left = np.polyfit(eff_y_list_plot[0],eff_x_list_plot[0],degree)
    equation_func_eff_left = np.poly1d(coefficients_eff_left)
    x_y_check_eff_left = equation_func_eff_left(Head_input)

    coefficients_eff_right = np.polyfit(eff_y_list_plot[rightSelcet],eff_x_list_plot[rightSelcet],degree)
    equation_func_eff_right = np.poly1d(coefficients_eff_right)
    x_y_check_eff_right = equation_func_eff_right(Head_input)

    # print('x_y_check_eff_left',x_y_check_eff_left)
    # print('x_y_check_eff_right',x_y_check_eff_right)

    try:
        x, y = flow_input, Head_input
        # print(x,y)
        # print(x_max,x_min,y_max,y_min)
        # (x > x_max or x < x_min or y > y_max or y < y_min)
        if y_value_top < Head_input or Head_input < y_value_botton or Head_input < y_value_center:
            print("NOT PASS",fac_number)
            pass
        elif x_y_check_eff_left < flow_input:
            print("PASS",fac_number)
            target = np.array([x, y])
            # print(target)
            def closest(lst, K):
                lst = np.array(lst)
                idx = (np.abs(lst - K)).argmin()
                return lst[idx]
            def closest_point(points, target):
                distances = np.sqrt(np.sum((points - target) ** 2, axis=1))
                closest_index = np.argmin(distances)
                return points[closest_index]
            # Impeller dimension
            # ### imp_1
            # imp_x_new_1 = np.linspace(min(imp_x_1), max(imp_x_1), num=100)
            # imp_y_new_1 = np.interp(imp_x_new_1, imp_x_1, imp_y_1)

            # new_points_imp_x_y_1 = [(x, y) for x, y in zip(imp_x_new_1, imp_y_new_1)]

            # ### imp_2
            # imp_x_new_2 = np.linspace(min(imp_x_2), max(imp_x_2), num=100)
            # imp_y_new_2 = np.interp(imp_x_new_2, imp_x_2, imp_y_2)

            # new_points_imp_x_y_2 = [(x, y) for x, y in zip(imp_x_new_2, imp_y_new_2)]

            # ### imp_3
            # imp_x_new_3 = np.linspace(min(imp_x_3), max(imp_x_3), num=100)
            # imp_y_new_3 = np.interp(imp_x_new_3, imp_x_3, imp_y_3)

            # new_points_imp_x_y_3 = [(x, y) for x, y in zip(imp_x_new_3, imp_y_new_3)]

            # ### imp_4
            # imp_x_new_4 = np.linspace(min(imp_x_4), max(imp_x_4), num=100)
            # imp_y_new_4 = np.interp(imp_x_new_4, imp_x_4, imp_y_4)

            # new_points_imp_x_y_4 = [(x, y) for x, y in zip(imp_x_new_4, imp_y_new_4)]
            # ### imp_5
            # imp_x_new_5 = np.linspace(min(imp_x_5), max(imp_x_5), num=100)
            # imp_y_new_5 = np.interp(imp_x_new_5, imp_x_5, imp_y_5)

            # new_points_imp_x_y_5 = [(x, y) for x, y in zip(imp_x_new_5, imp_y_new_5)]
            # ### imp_6
            # imp_x_new_6 = np.linspace(min(imp_x_6), max(imp_x_6), num=100)
            # imp_y_new_6 = np.interp(imp_x_new_6, imp_x_6, imp_y_6)

            # new_points_imp_x_y_6 = [(x, y) for x, y in zip(imp_x_new_6, imp_y_new_6)]
            # ### imp_7
            # imp_x_new_7 = np.linspace(min(imp_x_7), max(imp_x_7), num=100)
            # imp_y_new_7 = np.interp(imp_x_new_7, imp_x_7, imp_y_7)

            # new_points_imp_x_y_7 = [(x, y) for x, y in zip(imp_x_new_7, imp_y_new_7)]
            # ### imp_8
            # imp_x_new_8 = np.linspace(min(imp_x_8), max(imp_x_8), num=100)
            # imp_y_new_8 = np.interp(imp_x_new_8, imp_x_8, imp_y_8)

            # new_points_imp_x_y_8 = [(x, y) for x, y in zip(imp_x_new_8, imp_y_new_8)]
            # ### imp_9
            # imp_x_new_9 = np.linspace(min(imp_x_9), max(imp_x_9), num=100)
            # imp_y_new_9 = np.interp(imp_x_new_9, imp_x_9, imp_y_9)

            # new_points_imp_x_y_9 = [(x, y) for x, y in zip(imp_x_new_9, imp_y_new_9)]
            # # print(im_size_lst)
            # try:
            #     imp_list_fir = []
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_1, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_2, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_3, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_4, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_5, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_6, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_7, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_8, target))
            #     imp_list_fir.append(closest_point(new_points_imp_x_y_9, target))
            # except:
            #     pass
            coefficients = []
            equation_func = []
            x_y_check = []
            # print(im_size_lst,"..................")
            for i in range(len(im_size_lst)):
                coefficients.append(np.polyfit(imp_data_x[i], imp_data_y[i], degree))
                
                equation_func.append(np.poly1d(coefficients[i]))
                
                x_y_check.append((flow_input,equation_func[i](flow_input)))
                
            # print("new_points_imp_x_y_6", new_points_imp_x_y_1)
            # print(target, "target")
            # print("imp_list_fir", imp_list_fir)

            imp_near_x_y1 = np.array(closest_point(x_y_check, target))
            
            imp_in_near_x_y1 = [i for i, value in enumerate(x_y_check) if value[0] == imp_near_x_y1[0] and value[1] == imp_near_x_y1[1]]
            imp_in_near_x_y1 = imp_in_near_x_y1[0]
            x_y_check[imp_in_near_x_y1] = 0, 0
            imp_near_x_y2 = np.array(closest_point(x_y_check, target))
            imp_in_near_x_y2 = [i for i, value in enumerate(x_y_check) if value[0] == imp_near_x_y2[0] and value[1] == imp_near_x_y2[1]]
            imp_in_near_x_y2 = imp_in_near_x_y2[0]


            # print("imp_in_near_x_y1",im_size_lst[imp_in_near_x_y1])
            # print("imp_in_near_x_y2",im_size_lst[imp_in_near_x_y2])
            # print("imp_near_x_y1",imp_near_x_y1)
            # print("imp_near_x_y2",imp_near_x_y2)

            imp_dis_unit = abs(
                im_size_lst[imp_in_near_x_y1] - im_size_lst[imp_in_near_x_y2]
            )
            imp_d1 = math.sqrt(
                (imp_near_x_y2[0] - imp_near_x_y1[0]) ** 2
                + (imp_near_x_y2[1] - imp_near_x_y1[1]) ** 2
            )
            imp_d2 = math.sqrt(
                (imp_near_x_y1[0] - target[0]) ** 2 + (imp_near_x_y1[1] - target[1]) ** 2
            )

            # print("im_size_lst[imp_in_near_x_y1]", im_size_lst[imp_in_near_x_y1])
            # print("im_size_lst[imp_in_near_x_y2]", im_size_lst[imp_in_near_x_y2])
            # print("imp_dis_unit",imp_dis_unit)
            # print("imp_d1",imp_d1)
            # print("imp_d2",imp_d2)

            imp_dis_all = math.sqrt(
                (imp_near_x_y2[0] - imp_near_x_y1[0]) ** 2
                + (imp_near_x_y2[1] - imp_near_x_y1[1]) ** 2
            )

            imp_dis_clo_1 = math.sqrt(
                (imp_near_x_y1[0] - target[0]) ** 2 + (imp_near_x_y1[1] - target[1]) ** 2
            )

            imp_dis_clo_2 = math.sqrt(
                (imp_near_x_y2[0] - target[0]) ** 2 + (imp_near_x_y2[1] - target[1]) ** 2
            )

            # print("imp_dis_all", imp_dis_all)
            # print("imp_dis_clo_1", imp_dis_clo_1)
            # print("imp_dis_clo_2", imp_dis_clo_2)

            imp_test = abs((imp_near_x_y1[1]-y) /y) * 100
            # print(imp_test)
            if imp_test < 1:
                imp_output = im_size_lst[imp_in_near_x_y1]

            elif imp_dis_all < imp_dis_clo_2:
                imp_output = abs((imp_dis_unit * imp_d2 / imp_d1) + im_size_lst[imp_in_near_x_y1])

            elif imp_dis_all > imp_dis_clo_2:
                imp_output = abs((imp_dis_unit * imp_d2 / imp_d1) - im_size_lst[imp_in_near_x_y1])

            # print("Impeller dimension is %f mm" % (imp_output))
            if imp_output < min(im_size_lst) or imp_output > max(im_size_lst):
                return

            ####KW power

            ####kw
            n_x1 = closest(kw_size_lst, imp_output)
            t1 = kw_size_lst.index(n_x1)
            kw_size_lst[t1] = 0
            n_x2 = closest(kw_size_lst, imp_output)
            t2 = kw_size_lst.index(n_x2)

            kw_x1 = power_data_x[t1]
            kw_y1 = power_data_y[t1]
            near_x1 = closest(kw_x1, x)
            k1 = kw_x1.index(near_x1)
            near_y1 = kw_y1[k1]

            kw_x2 = power_data_x[t2]
            kw_y2 = power_data_y[t2]
            near_x2 = closest(kw_x2, x)
            k2 = kw_x2.index(near_x2)
            near_y2 = kw_y2[k2]

            dis_y_all = abs(near_y2 - near_y1)
            dis_unit = abs(n_x1 - n_x2)

            dis_y_unit = dis_y_all / dis_unit

            if n_x1 > n_x2:
                power = abs(dis_y_unit - near_y1)

            elif n_x1 < n_x2:
                power = abs(dis_y_unit + near_y1)

            # print('Power requirment = %f kW' %(power))

            ## Efficiency
            combiend_eff1 = list(zip(eff_data_x[0], eff_data_y[0]))
            combiend_eff2 = list(zip(eff_data_x[1], eff_data_y[1]))
            combiend_eff3 = list(zip(eff_data_x[2], eff_data_y[2]))
            combiend_eff4 = list(zip(eff_data_x[3], eff_data_y[3]))
            combiend_eff5 = list(zip(eff_data_x[4], eff_data_y[4]))
            combiend_eff6 = list(zip(eff_data_x[5], eff_data_y[5]))
            combiend_eff7 = list(zip(eff_data_x[6], eff_data_y[6]))
            combiend_eff8 = list(zip(eff_data_x[7], eff_data_y[7]))
            combiend_eff9 = list(zip(eff_data_x[8], eff_data_y[8]))
            
            try:
                eff_list_fir = []
                eff_list_fir.append(closest_point(combiend_eff1, target))
                eff_list_fir.append(closest_point(combiend_eff2, target))
                eff_list_fir.append(closest_point(combiend_eff3, target))
                eff_list_fir.append(closest_point(combiend_eff4, target))
                eff_list_fir.append(closest_point(combiend_eff5, target))
                eff_list_fir.append(closest_point(combiend_eff6, target))
                eff_list_fir.append(closest_point(combiend_eff7, target))
                eff_list_fir.append(closest_point(combiend_eff8, target))
                eff_list_fir.append(closest_point(combiend_eff9, target))
            except:
                pass
            
            coefficients_eff = []
            equation_func_eff = []
            x_y_check_eff = []
            for i in range(len(eff_size_lst)):
                coefficients_eff.append(np.polyfit(eff_data_y[i],eff_data_x[i],degree))
                equation_func_eff.append(np.poly1d(coefficients_eff[i]))
                x_y_check_eff.append((equation_func_eff[i](Head_input),Head_input))
            
            eff_near_x_y1 = np.array(closest_point(x_y_check_eff, target))
            eff_in_near_x_y1 = [i for i, value in enumerate(x_y_check_eff) if value[0] == eff_near_x_y1[0] and value[1] == eff_near_x_y1[1]]
            eff_in_near_x_y1 = eff_in_near_x_y1[0]
            eff_near_x_y1 = eff_list_fir[eff_in_near_x_y1]
            x_y_check_eff[eff_in_near_x_y1] = 0, 0

            eff_near_x_y2 = np.array(closest_point(x_y_check_eff, target))
            eff_in_near_x_y2 = [i for i, value in enumerate(x_y_check_eff) if value[0] == eff_near_x_y2[0] and value[1] == eff_near_x_y2[1]]
            eff_in_near_x_y2 = eff_in_near_x_y2[0]
            eff_near_x_y2 = eff_list_fir[eff_in_near_x_y2]
        
            
            # print("eff_size_lst",eff_size_lst)
            # print("eff_near_x_y2",eff_near_x_y2)
            # print("eff_size_lst[eff_in_near_x_y1]",eff_size_lst[eff_in_near_x_y1])
            # print("eff_size_lst[eff_in_near_x_y2]",eff_size_lst[eff_in_near_x_y2])
            eff_dis_all = math.sqrt(
                (eff_near_x_y2[0] - eff_near_x_y1[0]) ** 2
                + (eff_near_x_y2[1] - eff_near_x_y1[1]) ** 2
            )

            eff_dis_clo_1 = math.sqrt(
                (eff_near_x_y1[0] - target[0]) ** 2 + (eff_near_x_y1[1] - target[1]) ** 2
            )

            eff_dis_clo_2 = math.sqrt(
                (eff_near_x_y2[0] - target[0]) ** 2 + (eff_near_x_y2[1] - target[1]) ** 2
            )

            # print("eff_dis_all",eff_dis_all)
            # print("eff_dis_clo_1",eff_dis_clo_1)
            # print("eff_dis_clo_2",eff_dis_clo_2)

            eff_dis_unit = abs(
                eff_size_lst[eff_in_near_x_y1] - eff_size_lst[eff_in_near_x_y2]
            )
            eff_d1 = math.sqrt(
                (eff_near_x_y2[0] - eff_near_x_y1[0]) ** 2
                + (eff_near_x_y2[1] - eff_near_x_y1[1]) ** 2
            )
            eff_d2 = math.sqrt(
                (eff_near_x_y1[0] - target[0]) ** 2 + (eff_near_x_y1[1] - target[1]) ** 2
            )
            if eff_size_lst[eff_in_near_x_y1] > eff_size_lst[eff_in_near_x_y2]:
                if eff_dis_all < eff_dis_clo_2 and eff_dis_all < eff_dis_clo_1:
                    # print("[.....................]")
                    return
                if eff_dis_all < eff_dis_clo_2:
                    eff_output = abs(
                        (eff_dis_unit * eff_d2 / eff_d1) + eff_size_lst[eff_in_near_x_y1]
                    )
                elif eff_dis_all > eff_dis_clo_2:
                    eff_output = abs(
                        (eff_dis_unit * eff_d2 / eff_d1) - eff_size_lst[eff_in_near_x_y1]
                    )

            elif eff_size_lst[eff_in_near_x_y1] < eff_size_lst[eff_in_near_x_y2]:
                if eff_dis_all < eff_dis_clo_2 and eff_dis_all < eff_dis_clo_1:
                    # print("[.....................]")
                    return
                if eff_dis_all < eff_dis_clo_2:
                    eff_output = abs(
                        (eff_dis_unit * eff_d2 / eff_d1) - eff_size_lst[eff_in_near_x_y1]
                    )
                elif eff_dis_all > eff_dis_clo_2:
                    eff_output = abs(
                        (eff_dis_unit * eff_d2 / eff_d1) + eff_size_lst[eff_in_near_x_y1]
                    )
                # print('Efficiency is = %f percent'%(eff_output))
            


            combiend_npshr1 = list(zip(npshr_data_x[0], npshr_data_y[0]))
            combiend_npshr2 = list(zip(npshr_data_x[1], npshr_data_y[1]))
            combiend_npshr3 = list(zip(npshr_data_x[2], npshr_data_y[2]))
            combiend_npshr4 = list(zip(npshr_data_x[3], npshr_data_y[3]))
            combiend_npshr5 = list(zip(npshr_data_x[4], npshr_data_y[4]))
            combiend_npshr6 = list(zip(npshr_data_x[5], npshr_data_y[5]))
            combiend_npshr7 = list(zip(npshr_data_x[6], npshr_data_y[6]))
            combiend_npshr8 = list(zip(npshr_data_x[7], npshr_data_y[7]))

            try:
                npshr_list_fir = []
                npshr_list_fir.append(closest_point(combiend_npshr1, target))
                npshr_list_fir.append(closest_point(combiend_npshr2, target))
                npshr_list_fir.append(closest_point(combiend_npshr3, target))
                npshr_list_fir.append(closest_point(combiend_npshr4, target))
                npshr_list_fir.append(closest_point(combiend_npshr5, target))
                npshr_list_fir.append(closest_point(combiend_npshr6, target))
                npshr_list_fir.append(closest_point(combiend_npshr7, target))
                npshr_list_fir.append(closest_point(combiend_npshr8, target))

            except:
                pass
            # print(npshr_size_lst)
            # print("npshr_list_fir",npshr_list_fir)
            coefficients_npshr = []
            equation_func_npshr = []
            x_y_check_npshr = []
            for i in range(len(npshr_size_lst)):
                coefficients_npshr.append(np.polyfit(npshr_data_x[i],npshr_data_y[i],4))
                equation_func_npshr.append(np.poly1d(coefficients_npshr[i]))
                x_y_check_npshr.append((flow_input,equation_func_npshr[i](flow_input)))

            # npshr_near_x_y1 = np.array(closest_point(x_y_check_npshr, target))
            # print('x_y_check_npshr',x_y_check_npshr)
            # npshr_in_near_x_y1 = [i for i, value in enumerate(x_y_check_npshr) if value[0] == npshr_near_x_y1[0] and value[1] == npshr_near_x_y1[1]]
            # npshr_in_near_x_y1 = npshr_in_near_x_y1[0]
            # x_y_check_npshr[npshr_in_near_x_y1] = 0, 0


            npshr_near_x_y1 = np.array(closest_point(x_y_check_npshr, target))
            npshr_in_near_x_y1 = [i for i, value in enumerate(x_y_check_npshr) if value[0] == npshr_near_x_y1[0] and value[1] == npshr_near_x_y1[1]]
            npshr_in_near_x_y1 = npshr_in_near_x_y1[0]
            npshr_near_x_y1 = npshr_list_fir[npshr_in_near_x_y1]
            x_y_check_npshr[npshr_in_near_x_y1] = 0, 0
            
            npshr_in_near_x_y2 = npshr_in_near_x_y1 - 1
            npshr_near_x_y2 = x_y_check_npshr[npshr_in_near_x_y2]

            try:
                if npshr_in_near_x_y2 == -1:
                    npshr_in_near_x_y2 = + 1
                    npshr_near_x_y2 = npshr_list_fir[npshr_in_near_x_y2]


                npshr_dis_unit = abs(
                    npshr_size_lst[npshr_in_near_x_y1] - npshr_size_lst[npshr_in_near_x_y2]
                )
                npshr_d1 = math.sqrt(
                    (npshr_near_x_y2[0] - npshr_near_x_y1[0]) ** 2
                    + (npshr_near_x_y2[1] - npshr_near_x_y1[1]) ** 2
                )
                npshr_d2 = math.sqrt(
                    (npshr_near_x_y1[0] - target[0]) ** 2 + (npshr_near_x_y1[1] - target[1]) ** 2
                )


                npshr_dis_all = math.sqrt(
                    (npshr_near_x_y2[0] - npshr_near_x_y1[0]) ** 2
                    + (npshr_near_x_y2[1] - npshr_near_x_y1[1]) ** 2
                )

                npshr_dis_clo_1 = math.sqrt(
                    (npshr_near_x_y1[0] - target[0]) ** 2 + (npshr_near_x_y1[1] - target[1]) ** 2
                )

                npshr_dis_clo_2 = math.sqrt(
                    (npshr_near_x_y2[0] - target[0]) ** 2 + (npshr_near_x_y2[1] - target[1]) ** 2
                )

                if npshr_size_lst[npshr_in_near_x_y1] < npshr_size_lst[npshr_in_near_x_y2] and npshr_dis_all < npshr_dis_clo_2:
                    npshr_output = abs((npshr_dis_unit * npshr_d2 / npshr_d1) - npshr_size_lst[npshr_in_near_x_y1])
                elif npshr_size_lst[npshr_in_near_x_y1] < npshr_size_lst[npshr_in_near_x_y2] and npshr_dis_all > npshr_dis_clo_2:
                    npshr_output = abs((npshr_dis_unit * eff_d2 / eff_d1) + npshr_size_lst[npshr_in_near_x_y1])

                elif npshr_dis_all < npshr_dis_clo_2:
                    npshr_output = abs((npshr_dis_unit * npshr_d2 / npshr_d1) + npshr_size_lst[npshr_in_near_x_y1])

                elif npshr_dis_all > npshr_dis_clo_2:
                    npshr_output = abs((npshr_dis_unit * npshr_d2 / npshr_d1) - npshr_size_lst[npshr_in_near_x_y1])

                # print('NPSHr is %f m'%npshr_output)

            except IndexError:
                npshr_near_x = closest(npshr_x_1, x)
                npshr_near_in = npshr_x_1.index(npshr_near_x)
                npshr_output = npshr_y_1[npshr_near_in]
                # print("มา")
            # print('NPSHr is %f m'%npshr_output)


            name = dfmax.query(f"fac_number == '{fac_number}'")["model"].unique()
            chart = get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst_plot,eff_x_list_plot,eff_y_list_plot,eff_size_lst,eff_x_list,eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_output)
            # print("Impeller dimension is %f mm" % (imp_output))
            # print('Power requirment = %f kW' %(power))
            # print("Efficiency is = %f percent" % (eff_output))
            # print('NPSHr is %f m'%npshr_output)
            return name, imp_output, eff_output, power, npshr_output,chart
    except:
        pass

def get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst_plot,eff_x_list_plot,eff_y_list_plot,eff_size_lst,eff_x_list,eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_output):
    fix, ax = plt.subplots(figsize=(10,10))
    # plt.switch_backend('AGG')
    for i in range(len(im_size_lst)):
        ax.plot(imp_data_x[i], imp_data_y[i],linewidth=1,color='black')
        
    # for i in range(len(eff_size_lst)):
    #     plt.plot(eff_x_list[i], eff_y_list[i],)
    for i in range(len(eff_size_lst_plot)):
        ax.plot(eff_x_list_plot[i], eff_y_list_plot[i],linewidth=1, color='blue')
    ax.set_ylabel("Head")
    ax.set_xlabel("Flow")
    plt.title(name)
    for i in range(len(im_size_lst)):
        ax.text(imp_data_x[i][0], imp_data_y[i][0], f"{im_size_lst[i]}mm")
    for i in range(len(eff_size_lst)):
        ax.text(eff_x_list[i][0], eff_y_list[i]
                 [0], f"{eff_size_lst[i]}%")
        ax.text(eff_x_list[i][-1], eff_y_list[i]
                 [-1], f"{eff_size_lst[i]}%")
    ax.plot(flow_input, Head_input, marker='.', markersize=7,color='red')
    ax.text(0, 0, f"Fac-number: {fac_number}\nFlow: {flow_input}\nHead: {Head_input}\nImpeller dimension: {imp_output:.2f}mm\nEfficiency: {eff_output:.2f} %\nPower requirement: {power:.2f} kw\nNPSHr: {npshr_output:.2f} m")
    flow_chart = flow_input
    head_chart = Head_input
    x_head_input = []
    y_head_input = []
    while head_chart > 0.0:
        x_head_input.append(flow_input)
        y_head_input.append(head_chart - 0.1)
        head_chart -= 0.1
    ax.plot(x_head_input, y_head_input, color='red',linewidth=1)
    # print(x_head_input, y_head_input)
    x_flow_input = []
    y_flow_input = []
    while flow_chart > 0.0:
        x_flow_input.append(flow_chart - 0.1)
        y_flow_input.append(Head_input)
        flow_chart -= 0.1
    ax.plot(x_flow_input, y_flow_input,color='red',linewidth=1)
    # plt.xticks(rotation=45)
    ax.minorticks_on()
    
    ax.grid(True, which='both')

    graph = get_graph()
    return graph


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png',dpi=500)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# mydb = mysql.connector.connect(
#     host="project1.ts2337.com",
#     user="tscom_project1",
#     password="bzCUqyLI5ggZ",
#     database="tscom_project1"
# )
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="pea_detail_pump"
# )
# dfmax = pd.read_sql(
#                     f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table WHERE model_short LIKE "%MAX%" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)


# loaddata_max3('FAC-0175',400,13,dfmax)