import base64
from io import BytesIO
import matplotlib.pyplot as plt
import math
import pandas as pd
import mysql.connector
def loaddata_kdin(fac_number, fflow, hhead, dfkdin):
    import numpy as np

    ###imp
    imp_x_list = []
    imp_y_list = []
    im_size_lst = (
        dfkdin.query(f"data_type == 'QH' and fac_number == '{fac_number}'")[
            "imp_dia"
        ]
        .unique()
        .tolist()
    )
    name = dfkdin.query(f"fac_number == '{fac_number}'")["model"].unique()

    # print("name_id",name_id)
    for imp_dia in im_size_lst:
        flows = dfkdin.query(
            f"data_type == 'QH' and imp_dia == {imp_dia} and fac_number == '{fac_number}'"
        )["flow"].tolist()
        imp_x_list.append(flows)
        

        heads = dfkdin.query(
            f"data_type == 'QH' and imp_dia == {imp_dia} and fac_number == '{fac_number}'"
        )["head"].tolist()
        imp_y_list.append(heads)

    # print("im_size_lst",im_size_lst)
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
    # print(flow_list)
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
    # print(imp_data_x)
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
    # print(imp_data_y)
    ###########################################
    ### kw
    power_x_list = []
    power_y_list = []

    kw_size_lst = (
        dfkdin.query(f"data_type == 'KW' and fac_number == '{fac_number}'")[
            "imp_dia"
        ]
        .unique()
        .tolist()
    )
    for kw_dia in kw_size_lst:
        flows = dfkdin.query(
            f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
        )["flow"].tolist()
        power_x_list.append(flows)

        heads = dfkdin.query(
            f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
        )["kw"].tolist()
        power_y_list.append(heads)

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
        dfkdin.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")[
            "imp_dia"
        ]
        .unique()
        .tolist()
    )
    # print(npshr_size_lst)
    for im_size in npshr_size_lst:
        flow_n = dfkdin.query(
            f"data_type =='NPSHR'and fac_number == '{fac_number}'and imp_dia =={im_size}"
        )["flow"].tolist()
        npshr_x_list.append(flow_n)

        head_n = dfkdin.query(
            f"data_type =='NPSHR' and fac_number == '{fac_number}'and imp_dia =={im_size}"
        )["npshr"].tolist()
        npshr_y_list.append(head_n)

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

    (
        npshr_y_1,
        npshr_y_2,
        npshr_y_3,
        npshr_y_4,
        npshr_y_5,
        npshr_y_6,
        npshr_y_7,
        npshr_y_8,
        npshr_y_9,
    ) = npshr_y_list + [[0]] * (9 - len(npshr_size_lst))

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
        dfkdin.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")["eff"]
        .unique()
        .tolist()
    )

    for eff_size in eff_size_lst:
        eff_flow = (
            dfkdin.query(
                f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["flow"]
            .tolist()
        )

        eff_x_list.append(eff_flow)

        # eff_flow_list.sort()
        eff_head = (
            dfkdin.query(
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

    # Impeller
    try:
        x, y = flow_input, Head_input
        if x > x_max or x < x_min or y > y_max or y < y_min:
            # print("out of range fir")

            pass
        else:
            target = np.array([x, y])

            def closest(lst, K):
                lst = np.array(lst)
                idx = (np.abs(lst - K)).argmin()
                return lst[idx]

            def closest_point(points, target):
                distances = np.sqrt(np.sum((points - target) ** 2, axis=1))
                closest_index = np.argmin(distances)
                return points[closest_index]

            ###################################################################################

            # Impeller dimension
            ### imp_1
            imp_x_new_1 = np.linspace(min(imp_x_1), max(imp_x_1), num=100)
            imp_y_new_1 = np.interp(imp_x_new_1, imp_x_1, imp_y_1)

            new_points_imp_x_y_1 = [(x, y) for x, y in zip(imp_x_new_1, imp_y_new_1)]

            ### imp_2
            imp_x_new_2 = np.linspace(min(imp_x_2), max(imp_x_2), num=100)
            imp_y_new_2 = np.interp(imp_x_new_2, imp_x_2, imp_y_2)

            new_points_imp_x_y_2 = [(x, y) for x, y in zip(imp_x_new_2, imp_y_new_2)]

            ### imp_3
            imp_x_new_3 = np.linspace(min(imp_x_3), max(imp_x_3), num=100)
            imp_y_new_3 = np.interp(imp_x_new_3, imp_x_3, imp_y_3)

            new_points_imp_x_y_3 = [(x, y) for x, y in zip(imp_x_new_3, imp_y_new_3)]

            ### imp_4
            imp_x_new_4 = np.linspace(min(imp_x_4), max(imp_x_4), num=100)
            imp_y_new_4 = np.interp(imp_x_new_4, imp_x_4, imp_y_4)

            new_points_imp_x_y_4 = [(x, y) for x, y in zip(imp_x_new_4, imp_y_new_4)]
            ### imp_5
            imp_x_new_5 = np.linspace(min(imp_x_5), max(imp_x_5), num=100)
            imp_y_new_5 = np.interp(imp_x_new_5, imp_x_5, imp_y_5)

            new_points_imp_x_y_5 = [(x, y) for x, y in zip(imp_x_new_5, imp_y_new_5)]
            ### imp_6
            imp_x_new_6 = np.linspace(min(imp_x_6), max(imp_x_6), num=100)
            imp_y_new_6 = np.interp(imp_x_new_6, imp_x_6, imp_y_6)

            new_points_imp_x_y_6 = [(x, y) for x, y in zip(imp_x_new_6, imp_y_new_6)]
            ### imp_7
            imp_x_new_7 = np.linspace(min(imp_x_7), max(imp_x_7), num=100)
            imp_y_new_7 = np.interp(imp_x_new_7, imp_x_7, imp_y_7)

            new_points_imp_x_y_7 = [(x, y) for x, y in zip(imp_x_new_7, imp_y_new_7)]
            ### imp_8
            imp_x_new_8 = np.linspace(min(imp_x_8), max(imp_x_8), num=100)
            imp_y_new_8 = np.interp(imp_x_new_8, imp_x_8, imp_y_8)

            new_points_imp_x_y_8 = [(x, y) for x, y in zip(imp_x_new_8, imp_y_new_8)]
            ### imp_9
            imp_x_new_9 = np.linspace(min(imp_x_9), max(imp_x_9), num=100)
            imp_y_new_9 = np.interp(imp_x_new_9, imp_x_9, imp_y_9)

            new_points_imp_x_y_9 = [(x, y) for x, y in zip(imp_x_new_9, imp_y_new_9)]

            try:
                imp_list_fir = []
                imp_list_fir.append(closest_point(new_points_imp_x_y_1, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_2, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_3, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_4, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_5, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_6, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_7, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_8, target))
                imp_list_fir.append(closest_point(new_points_imp_x_y_9, target))
            except:
                pass
            # print("new_points_imp_x_y_6", new_points_imp_x_y_6)
            # print(target, "target")
            # print("imp_list_fir", imp_list_fir)

            imp_near_x_y1 = np.array(closest_point(imp_list_fir, target))

            imp_in_near_x_y1 = [i for i, value in enumerate(imp_list_fir) if value[0] == imp_near_x_y1[0] and value[1] == imp_near_x_y1[1]]
            imp_in_near_x_y1 = imp_in_near_x_y1[0]

            imp_list_fir[imp_in_near_x_y1] = 0, 0
            # print(im_size_lst[imp_in_near_x_y1])
            imp_in_near_x_y2 = imp_in_near_x_y1 - 1
            imp_near_x_y2 = imp_list_fir[imp_in_near_x_y2]
            # print(im_size_lst[imp_in_near_x_y2])
            # print("imp_near_x_y1", imp_near_x_y1)
            # print("imp_near_x_y2", imp_near_x_y2)

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
            # if imp_test < 1:
            #     imp_output = im_size_lst[imp_in_near_x_y1]
            if imp_near_x_y2 == (0.0, 0.0):
                # print("ออก")
                return
            elif im_size_lst[imp_in_near_x_y1] > im_size_lst[imp_in_near_x_y2]:
                if imp_dis_all < imp_dis_clo_2:
                    imp_output = abs(
                        (imp_dis_unit * imp_d2 / imp_d1) + im_size_lst[imp_in_near_x_y1]
                    )
                elif imp_dis_all > imp_dis_clo_2:
                    imp_output = abs(
                        (imp_dis_unit * imp_d2 / imp_d1) - im_size_lst[imp_in_near_x_y1]
                    )

            elif im_size_lst[imp_in_near_x_y1] < im_size_lst[imp_in_near_x_y2]:
                if imp_dis_all < imp_dis_clo_2:
                    imp_output = abs(
                        (imp_dis_unit * imp_d2 / imp_d1) - im_size_lst[imp_in_near_x_y1]
                    )
                elif imp_dis_all > imp_dis_clo_2:
                    imp_output = abs(
                        (imp_dis_unit * imp_d2 / imp_d1) + im_size_lst[imp_in_near_x_y1]
                    )
            if imp_output > max(im_size_lst):
                # print("imp เกินกราฟ")
                return
            elif imp_output < min(im_size_lst):
                # print("imp ตกกราฟ")
                return
            # print("Fac-number",fac_number)
            # print("Impeller dimension is %f mm" % (imp_output))

            ####kw
            n_x1 = closest(kw_size_lst, imp_output)
            # print("kw",kw_size_lst)
            # print("imp_output",imp_output)
            t1 = kw_size_lst.index(n_x1)
            kw_size_lst[t1] = 0
            n_x2 = closest(kw_size_lst, imp_output)
            t2 = kw_size_lst.index(n_x2)

            # print("n_x1",n_x1)
            # print("n_x2",n_x2)
            # print("t1",t1)
            # print("t2",t2)
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
            # print("n_x1",n_x1)
            # print("n_x2",n_x2)
            # print("near_y1",near_y1)
            # print("near_y2",near_y2)
            dis_y_unit = dis_y_all / dis_unit
            # print("dis_y_unit",dis_y_unit)
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
            eff_near_x_y1 = np.array(closest_point(eff_list_fir, target))

            eff_in_near_x_y1 = [i for i, value in enumerate(eff_list_fir) if value[0] == eff_near_x_y1[0] and value[1] == eff_near_x_y1[1]]
            eff_in_near_x_y1 = eff_in_near_x_y1[0]

            eff_list_fir[eff_in_near_x_y1] = 0, 0

            # print("eff_in_near_x_y1", eff_in_near_x_y1)
            # print("eff_in_near_x_y2", eff_in_near_x_y2)

            # print("eff_list_fir", eff_list_fir)
            eff_near_x_y2 = np.array(closest_point(eff_list_fir, target))
            eff_in_near_x_y2 = [i for i, value in enumerate(eff_list_fir) if value[0] == eff_near_x_y2[0] and value[1] == eff_near_x_y2[1]]
            eff_in_near_x_y2 = eff_in_near_x_y2[0]
            # print("eff_list_fir",eff_list_fir)
            # print("eff_near_x_y1",eff_near_x_y1)
            # print("eff_near_x_y2",eff_near_x_y2)

            # print("eff_near_x_y1",eff_near_x_y1)
            # print("eff_near_x_y2",eff_near_x_y2)
            # print("eff_d1",eff_d1)
            # print("eff_d2",eff_d2)
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
            
            if eff_output >= max(eff_size_lst):
                eff_output = max(eff_size_lst)
            elif eff_output < min(eff_size_lst):
                # print("ค่าeffไม่ถึง")
                return
            # print("Efficiency is = %f percent" % (eff_output))

            # Power
            pgnq = (1000 * 9.81 * y * (x / 3600)) / 1000
            eff_pre = eff_output / 100
            power = pgnq / eff_pre
            # print("Power requirment = %f kW" % (power))

            # NPSHR
            npshr_near_x = closest(npshr_x_1, x)
            npshr_near_in = npshr_x_1.index(npshr_near_x)
            npshr_near_y = npshr_y_1[npshr_near_in]
            # for i in range(len(im_size_lst)):
            #     plt.plot(imp_data_x[i], imp_data_y[i])
            # for i in range(len(eff_size_lst)):
            #     plt.plot(eff_x_list[i], eff_y_list[i],)
            # plt.ylabel("Head")
            # plt.xlabel("Flow")
            # plt.title(name)
            # for i in range(len(im_size_lst)):
            #     plt.text(imp_data_x[i][0], imp_data_y[i][0], f"{im_size_lst[i]}mm")
            # for i in range(len(eff_size_lst)):
            #     plt.text(eff_x_list[i][0], eff_y_list[i]
            #             [0], f"{eff_size_lst[i]}%")
            #     plt.text(eff_x_list[i][-1], eff_y_list[i]
            #             [-1], f"{eff_size_lst[i]}%")
            # plt.plot(flow_input, Head_input, marker='.', markersize=12)
            # plt.show()
            # print('NPSHr is %f m'%npshr_near_y)

    

            chart = get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst,eff_x_list,eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_near_y)
            # print("Impeller dimension is %f mm" % (imp_output))
            # print('Power requirment = %f kW' %(power))
            # print("Efficiency is = %f percent" % (eff_output))
            # print('NPSHr is %f m'%npshr_near_y)
           
            return name, imp_output, eff_output, power, npshr_near_y,chart
    except:
        pass


def get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst,eff_x_list,eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_output):
    plt.switch_backend('AGG')
    for i in range(len(im_size_lst)):
        plt.plot(imp_data_x[i], imp_data_y[i])
        
    for i in range(len(eff_size_lst)):
        plt.plot(eff_x_list[i], eff_y_list[i],)
    plt.ylabel("Head")
    plt.xlabel("Flow")
    plt.title(name)
    for i in range(len(im_size_lst)):
        plt.text(imp_data_x[i][0], imp_data_y[i][0], f"{im_size_lst[i]}mm")
    for i in range(len(eff_size_lst)):
        plt.text(eff_x_list[i][0], eff_y_list[i]
                 [0], f"{eff_size_lst[i]}%")
        plt.text(eff_x_list[i][-1], eff_y_list[i]
                 [-1], f"{eff_size_lst[i]}%")
    plt.plot(flow_input, Head_input, marker='.', markersize=12)
    plt.text(0, 0, f"Fac-number: {fac_number}\nFlow: {flow_input}\nHead: {Head_input}\nImpeller dimension: {imp_output:.2f}mm\nEfficiency: {eff_output:.2f} %\nPower requirement: {power:.2f} kw\nNPSHr: {npshr_output:.2f} m")
    flow_chart = flow_input
    head_chart = Head_input
    x_head_input = []
    y_head_input = []
    while head_chart > 0.0:
        x_head_input.append(flow_input)
        y_head_input.append(head_chart - 0.1)
        head_chart -= 0.1
    plt.plot(x_head_input, y_head_input)
    # print(x_head_input, y_head_input)
    x_flow_input = []
    y_flow_input = []
    while flow_chart > 0.0:
        x_flow_input.append(flow_chart - 0.1)
        y_flow_input.append(Head_input)
        flow_chart -= 0.1
    plt.plot(x_flow_input, y_flow_input)
    plt.xticks(rotation=45)

    graph = get_graph()
    return graph


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)



dfkdin = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence FROM factory_table where model_short = "KDIN"', con=mydb)

loaddata_kdin('FAC-0001', 45, 45,dfkdin)