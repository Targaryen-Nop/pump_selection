import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)
dfkdin = pd.read_sql(
    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence FROM factory_table where model_short = "KDIN"', con=mydb)


def loaddatamax5(fac_number, fflow, hhead, gtnum, eqnum, lessnum, df):
    # แสดงข้อมูล
    im_size_lst = df.query(f"data_type == 'QH' and fac_number == '{fac_number}'")[
        'imp_dia'].unique().tolist()
    eff_size_lst = df.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")[
        'eff'].unique().tolist()
    # print(eff_size_lst)

    head_list = []
    flow_list = []
    flow_p_list = []
    power_list = []
    eff_flow_list = []
    eff_head_list = []
    eff_i_list = []
    for imp_dia in im_size_lst:
        flows = df.query(f"data_type == 'QH' and imp_dia == {imp_dia}and fac_number == '{fac_number}'")[
            'flow'].tolist()
        flow_list.append(flows)

        heads = df.query(f"data_type == 'QH' and imp_dia == {imp_dia}and fac_number == '{fac_number}'")[
            'head'].tolist()
        head_list.append(heads)

        flow_p = df.query(f"data_type =='KW' and imp_dia =={imp_dia}and fac_number == '{fac_number}'")[
            'flow'].tolist()
        flow_p_list.append(flow_p)

        power = df.query(f"data_type =='KW' and imp_dia =={imp_dia}and fac_number == '{fac_number}'")[
            'kw'].tolist()
        power_list.append(power)

    for eff_size in eff_size_lst:
        eff_flow = df.query(f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'").sort_values(
            'se_quence', ascending=True)['flow'].tolist()

        eff_flow_list.append(eff_flow)

        # eff_flow_list.sort()
        eff_head = df.query(f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'").sort_values(
            'se_quence', ascending=True)['head'].tolist()
        eff_head_list.append(eff_head)
        # print(eff_flow_list[1])
        # print(eff_head_list[1])

        # eff_head_list.sort()

    # eff_flow_list[1].sort()
    # eff_head_list[1].sort(reverse=True)

    flow_n = df.query(f"data_type =='NPSHR'and fac_number == '{fac_number}'")[
        'flow'].unique().tolist()
    head_n = df.query(f"data_type =='NPSHR' and fac_number == '{fac_number}'")[
        'npshr'].unique().tolist()

    power_1, power_2, power_3, power_4, power_5, power_6, power_7, power_8, * \
        _ = power_list + [[0, 0]] * (8 - len(power_list))
    flow_p_1, flow_p_2, flow_p_3, flow_p_4, flow_p_5, flow_p_6, flow_p_7, flow_p_8 = flow_p_list + \
        [[0, 0]] * (8 - len(im_size_lst))

    flow1, flow2, flow3, flow4, flow5, flow6, flow7, flow8 = flow_list + \
        [[0, 0]] * (8 - len(im_size_lst))

    head1, head2, head3, head4, head5, head6, head7, head8 = head_list + \
        [[0, 0]] * (8 - len(im_size_lst))

    eff_flow1, eff_flow2, eff_flow3, eff_flow4, eff_flow5, eff_flow6, eff_flow7, eff_flow8 = eff_flow_list + \
        [None] * (8 - len(eff_flow_list))

    eff_head1, eff_head2, eff_head3, eff_head4, eff_head5, eff_head6, eff_head7, eff_head8 = eff_head_list + \
        [None] * (8 - len(eff_head_list))

   # Impeller
    im_data_flow = [flow1, flow2, flow3, flow4, flow5, flow6, flow7, flow8]
    im_data_head = [head1, head2, head3, head4, head5, head6, head7, head8]
    # Power
    flow_power = [flow_p_1, flow_p_2, flow_p_3,
                  flow_p_4, flow_p_5, flow_p_6, flow_p_7, flow_p_8]
    head_power = [power_1, power_2, power_3,
                  power_4, power_5, power_6, power_7, power_8]
    '----------------------------------------------------------------------'
    # inputsection
    flow_input = float(fflow)  # รอรับจากลูกค้า
    Head_input = float(hhead)  # รอรับจากลูกค้า
    name = df.query(f"fac_number =='{fac_number}'")['model'].unique()
    for i in range(len(im_size_lst)):
        plt.plot(flow_list[i], head_list[i])
    for i in range(len(eff_size_lst)):
        plt.plot(eff_flow_list[i], eff_head_list[i], )

    # # ตั้งชื่อแกน x และ y
    # plt.xlabel('x')
    # plt.ylabel('y')

    # plt.ylabel("Head")
    # plt.xlabel("Flow")
    # plt.title(name)
    # for i in range(len(im_size_lst)):
    #     plt.text(flow_list[i][0], head_list[i][0], f"{im_size_lst[i]}mm")
    # for i in range(len(eff_size_lst)):
    #     plt.text(eff_flow_list[i][0], eff_head_list[i]
    #              [0], f"{eff_size_lst[i]}%")
    #     plt.text(eff_flow_list[i][-1], eff_head_list[i]
    #              [-1], f"{eff_size_lst[i]}%")

    # plt.plot(flow_input, Head_input, marker='.', markersize=12)

    # flow_chart = flow_input
    # head_chart = Head_input
    # x_head_input = []
    # y_head_input = []
    # while head_chart > 0.0:
    #     x_head_input.append(flow_input)
    #     y_head_input.append(head_chart - 0.1)
    #     head_chart -= 0.1
    # plt.plot(x_head_input, y_head_input)
    # # print(x_head_input, y_head_input)
    # x_flow_input = []
    # y_flow_input = []
    # while flow_chart > 0.0:
    #     x_flow_input.append(flow_chart - 0.1)
    #     y_flow_input.append(Head_input)
    #     flow_chart -= 0.1
    # plt.plot(x_flow_input, y_flow_input)
    # plt.show()
    # print(eff_flow1)
    # print(eff_head1)
    ### edit every file ###
    name = df.query(f"fac_number =='{fac_number}'")['model'].unique()
    # print(name)
    x_max = float(
        (max([max(flow1), max(flow2), max(flow3), max(flow4), max(flow5), max(flow6), max(flow7), max(flow8)])))
    x_min = float(
        (min([min(flow1), min(flow2), min(flow3), min(flow4), min(flow5), min(flow6), min(flow7), min(flow8)])))
    y_max = float(
        (max([max(head1), max(head2), max(head3), max(head4), max(head5), max(head6), max(head7), max(head8)])))
    y_min = float(
        (min([min(head1), min(head2), min(head3), min(head4), min(head5), min(head6), min(head7), min(head8)])))
    head = [head1, head2, head3, head4, head5, head6, head7, head8]

    try:
        # Impeller
        x, y = flow_input, Head_input

        if (x > x_max or x < x_min or y > y_max or y < y_min):
            # print("out of range")
            pass
        else:
            def closest(lst, K):
                lst = np.array(lst)
                idx = (np.abs(lst - K)).argmin()
                return lst[idx]

            i = []
            pos = []
            positive_pos = []
            negative_pos = []
            pos_y = []

            for j in range(len(im_data_flow)):
                i.append(closest(im_data_flow[j], x))
                pos.append(im_data_flow[j].index(i[j]))
                positive_pos.append(pos[j]+1)
                negative_pos.append(pos[j]-1)
                pos_y.append(head[j][pos[j]])

            nearest_y_1 = (closest(pos_y, y))
            u = pos_y.index(nearest_y_1)
            nearest_x_1 = i[u]

            flow_select, head_select = im_data_flow[u], im_data_head[u]

            nearest_x_p_1 = flow_select[positive_pos[u]]
            nearest_x_n_1 = flow_select[negative_pos[u]]
            nearest_y_p_1 = head_select[positive_pos[u]]
            nearest_y_n_1 = head_select[negative_pos[u]]

            ant_near_x_lst = [nearest_x_p_1, nearest_x_n_1]
            ant_near_y_lst = [nearest_y_p_1, nearest_y_n_1]
            ant_near_x_1 = (closest(ant_near_x_lst, x))
            pos_ant_near_x = ant_near_x_lst.index(ant_near_x_1)
            ant_near_y_1 = ant_near_y_lst[pos_ant_near_x]

            if y > ant_near_y_1:
                nearest_x_2 = i[u-1]
                v = u-1
            else:
                nearest_x_2 = i[u+1]
                v = u+1

            nearest_y_2 = pos_y[v]

            flow_select_2, head_select_2 = im_data_flow[v], im_data_head[v]

            nearest_x_p_2 = flow_select_2[positive_pos[v]]
            nearest_x_n_2 = flow_select_2[negative_pos[v]]
            nearest_y_p_2 = head_select_2[positive_pos[v]]
            nearest_y_n_2 = head_select_2[negative_pos[v]]

            ant_near_x_lst_2 = [nearest_x_p_2, nearest_x_n_2]
            ant_near_y_lst_2 = [nearest_y_p_2, nearest_y_n_2]
            ant_near_x_2 = (closest(ant_near_x_lst_2, x))
            pos_ant_near_x_2 = ant_near_x_lst_2.index(ant_near_x_2)
            ant_near_y_2 = ant_near_y_lst_2[pos_ant_near_x_2]

            x0 = nearest_x_1
            y0 = nearest_y_1
            x1 = ant_near_x_1
            y1 = ant_near_y_1
            xp = x
            yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)

            x2 = nearest_x_2
            y2 = nearest_y_2
            x3 = ant_near_x_2
            y3 = ant_near_y_2
            xs = x
            ys = y2 + ((y3-y2)/(x3-x2)) * (xs - x2)

            imsize_1 = im_size_lst[u]
            imsize_2 = im_size_lst[v]

            xi = yp
            yi = imsize_1
            xk = ys
            yk = imsize_2
            xh = y
            im_size = yi + ((yk-yi)/(xk-xi)) * (xh - xi)
            # print('Impeller dimension is %f mm' % (im_size))

            # power
            im_power = closest(im_size_lst, im_size)
            p = im_size_lst.index(im_power)
            flow_positon = flow_power[p]
            p_x = (closest(flow_positon, x))
            v = flow_positon.index(p_x)
            head_position = head_power[p]
            p_y = head_position[v]

            flow_ant_pos = [flow_power[p][v+1], flow_power[p][v-1]]
            ant_p_x = (closest(flow_ant_pos, x))
            w = flow_positon.index(ant_p_x)
            ant_p_y = head_position[w]

            if im_size > im_power:
                p_2 = p-1
            else:
                p_2 = p+1

            flow_positon_2 = flow_power[p_2]
            p_x_2 = (closest(flow_positon_2, x))
            v_2 = flow_positon_2.index(p_x_2)
            head_position_2 = head_power[p_2]
            p_y_2 = head_position_2[v_2]
            flow_ant_pos_2 = [flow_power[p_2][v_2+1], flow_power[p_2][v_2-1]]
            ant_p_x_2 = (closest(flow_ant_pos_2, x))
            w_2 = flow_positon_2.index(ant_p_x_2)
            ant_p_y_2 = head_position_2[w_2]

            x4 = p_x
            y4 = p_y
            x5 = ant_p_x
            y5 = ant_p_y
            xm = x
            ym = y4 + ((y5-y4)/(x5-x4)) * (xm - x4)

            x8 = p_x_2
            y8 = p_y_2
            x9 = ant_p_x_2
            y9 = ant_p_y_2
            xn = x
            yn = y8 + ((y9-y8)/(x9-x8)) * (xn - x8)

            xi = imsize_1
            yi = ym
            xk = imsize_2
            yk = yn
            xh = im_size
            power = yi + ((yk-yi)/(xk-xi)) * (xh - xi)
            # print('Power requirment = %f kW' % (power))

            # eff
            p_m = power
            S_G = 1000
            Q = (x/3600)
            g = 10
            p_p = ((S_G)*Q*g*y)/1000
            eff = ((p_p)/(p_m))*100
            # print('Efficiency is = %f percent' % (eff))

            # NPSHR
            n_x = closest(flow_n, x)
            t = flow_n.index(n_x)
            n_y = head_n[t]

            ant_flow_n = [flow_n[t+1], flow_n[t-1]]
            ant_n_x = closest(ant_flow_n, x)
            s = flow_n.index(ant_n_x)
            ant_n_y = head_n[s]

            x6 = n_x
            y6 = n_y
            x7 = ant_n_x
            y7 = ant_n_y
            xt = x
            yt = y6 + ((y7-y6)/(x7-x6)) * (xt - x6)
            # print('NPSHr is %f m'%yt)

            ### edit every file ###
            if eff > gtnum:  # รอ
                eff = eqnum  # รอ

            if im_size > im_size_lst[0] or im_size < im_size_lst[-1] or eff < lessnum:
                print("out of range")
                pass
            else:
                # print("\n### %s" % name)
                # print('Impeller dimension is %.2f mm' % (im_size))
                # print('Efficiency is = %.2f percent' % (eff))
                # print('Power requirment = %.2f kW' % (power))
                # print('NPSHr is %.2f m' % yt)

######################################################################################################
                for i in range(len(im_size_lst)):
                    plt.plot(flow_list[i], head_list[i])
                for i in range(len(eff_size_lst)):
                    plt.scatter(eff_flow_list[i], eff_head_list[i], s=1)
                plt.ylabel("Head")
                plt.xlabel("Flow")
                plt.title(name)
                for i in range(len(im_size_lst)):
                    plt.text(flow_list[i][0], head_list[i]
                             [0], f"{im_size_lst[i]}mm")
                for i in range(len(eff_size_lst)):
                    plt.text(eff_flow_list[i][0], eff_head_list[i]
                             [0], f"{eff_size_lst[i]}%")
                    plt.text(eff_flow_list[i][-1], eff_head_list[i]
                             [-1], f"{eff_size_lst[i]}%")

                plt.plot(flow_input, Head_input, marker='.', markersize=12)

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
                plt.show()
                return name, im_size, eff, power, yt
######################################################################################################

                # for i in range(len(im_size_lst)):
                #     plt.plot(flow_list[i], head_list[i])
                # for i in range(len(eff_size_lst)):
                #     plt.scatter(eff_flow_list[i], eff_head_list[i],s=1)
                # plt.ylabel("Head")
                # plt.xlabel("Flow")
                # plt.title(name)
                # for i in range(len(im_size_lst)):
                #     plt.text(flow_list[i][0], head_list[i][0], f"{im_size_lst[i]}mm")
                # for i in range(len(eff_size_lst)):
                #     plt.text(eff_flow_list[i][0], eff_head_list[i]
                #             [0], f"{eff_size_lst[i]}%")
                #     plt.text(eff_flow_list[i][-1], eff_head_list[i]
                #             [-1], f"{eff_size_lst[i]}%")

                # plt.plot(flow_input, Head_input, marker='.', markersize=12)

                # flow_chart = flow_input
                # head_chart = Head_input
                # x_head_input = []
                # y_head_input = []
                # while head_chart > 0.0:
                #     x_head_input.append(flow_input)
                #     y_head_input.append(head_chart - 0.1)
                #     head_chart -= 0.1
                # plt.plot(x_head_input, y_head_input)
                # # print(x_head_input, y_head_input)
                # x_flow_input = []
                # y_flow_input = []
                # while flow_chart > 0.0:
                #     x_flow_input.append(flow_chart - 0.1)
                #     y_flow_input.append(Head_input)
                #     flow_chart -= 0.1
                # plt.plot(x_flow_input, y_flow_input)
                # plt.show()

    except IndexError:
        pass


# fflow = 120
# hhead = 70
# loaddatamax5('FAC-0001', fflow, hhead, 58, 60, 50, dfkdin)
# loaddatamax5('FAC-0002', fflow, hhead, 62, 63, 51, dfkdin)
# loaddatamax5('FAC-0002', fflow, hhead, 57, 58, 45, dfkdin)
# loaddatamax5('FAC-0003', fflow, hhead, 49, 50, 40, dfkdin)
# loaddatamax5('FAC-0004', fflow, hhead, 40, 42, 30, dfkdin)
# loaddatamax5('FAC-0005', fflow, hhead, 73, 74, 61, dfkdin)
# loaddatamax5('FAC-0006', fflow, hhead, 62, 64, 48, dfkdin)
# loaddatamax5('FAC-0007', fflow, hhead, 59, 60, 57, dfkdin)
# loaddatamax5('FAC-0008', fflow, hhead, 53, 54, 42, dfkdin)
# loaddatamax5('FAC-0009', fflow, hhead, 43, 44, 33, dfkdin)
# loaddatamax5('FAC-0010', fflow, hhead, 77, 78, 64, dfkdin)
# loaddatamax5('FAC-0011', fflow, hhead, 73, 75, 51, dfkdin)
# loaddatamax5('FAC-0012', fflow, hhead, 69, 70, 50, dfkdin)
# loaddatamax5('FAC-0013', fflow, hhead, 59, 59, 49, dfkdin)
# loaddatamax5('FAC-0014', fflow, hhead, 62, 63, 50, dfkdin)
# loaddatamax5('FAC-0015', fflow, hhead, 60, 61, 49, dfkdin)
# loaddatamax5('FAC-0016', fflow, hhead, 78, 79.5, 69, dfkdin)
# loaddatamax5('FAC-0017', fflow, hhead, 73, 74, 60, dfkdin)
# loaddatamax5('FAC-0018', fflow, hhead, 73, 74, 56, dfkdin)
# loaddatamax5('FAC-0019', fflow, hhead, 72, 74, 58, dfkdin)
# loaddatamax5('FAC-0020', fflow, hhead, 64, 66, 40, dfkdin)
# loaddatamax5('FAC-0021', fflow, hhead, 78, 80, 56, dfkdin)
# loaddatamax5('FAC-0022', fflow, hhead, 77, 78, 53, dfkdin)
# loaddatamax5('FAC-0023', fflow, hhead, 75, 76, 57, dfkdin)
# loaddatamax5('FAC-0024', fflow, hhead, 73, 74, 51, dfkdin)
# loaddatamax5('FAC-0025', fflow, hhead, 76, 77, 64, dfkdin)
# loaddatamax5('FAC-0026', fflow, hhead, 79, 80, 60, dfkdin)
# loaddatamax5('FAC-0027', fflow, hhead, 76, 77, 61, dfkdin)
# loaddatamax5('FAC-0028', fflow, hhead, 73, 75, 62, dfkdin)
# loaddatamax5('FAC-0029', fflow, hhead, 72, 73.5, 61, dfkdin)
# loaddatamax5('FAC-0030', fflow, hhead, 84, 86, 60, dfkdin)
