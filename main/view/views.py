from django.shortcuts import render
from django.http import HttpResponse
from database.forms import MyForm
import pandas as pd
import mysql.connector
import numpy as np
import io
from pumpselection.view.kdin import loaddata_kdin
from pumpselection.view.kiso1 import loaddata_kiso
from pumpselection.view.kiso2 import loaddata_kiso_two
from pumpselection.view.kop import loaddata_kop9196
from pumpselection.view.max import loaddata_max3
from database.forms import SearchForm
from django.db.models import Q
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)



def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # ดำเนินการเพิ่มข้อมูลลงในฐานข้อมูลหรือส่งข้อมูลไปยังเซิร์ฟเวอร์ที่ต้องการ

        # ตัวอย่าง: ให้ส่งข้อมูลไปยังเซิร์ฟเวอร์ที่ใช้ API
        data = {
            'name': name,
            'email': email
        }
        response = requests.post('https://example.com/api/endpoint', data=data)
        if response.status_code == 200:
            # ดำเนินการเพิ่มข้อมูลสำเร็จ
            return HttpResponse('Data added successfully')
        else:
            # ดำเนินการเพิ่มข้อมูลไม่สำเร็จ
            return HttpResponse('Failed to add data: email={}, name={}'.format(email, name))

    # แสดงฟอร์มหากไม่ได้รับคำขอ POST
    return render(request, 'adddata.html')
def employee_search(request):
    if request.method == 'POST':
        kw = request.POST.get('fac_number', '')
        form = SearchForm(request.POST, initial={'fac_number': kw})
    else:
        kw = request.GET.get('name', '')
        form = SearchForm(initial={'name': kw})
        
    # ดึงข้อมูลจากฐานข้อมูลโดยใช้ Pandas
    factory_table = pd.read_sql('SELECT fac_number, equipment, brand, model_short, model, rpm FROM factory_table', con=mydb)
    
    # กรองข้อมูลโดยใช้ค่าที่รับเข้ามาจากแบบฟอร์ม Django
    filtered_data = factory_table[(factory_table['fac_number'].str.contains(kw)) |
                                  (factory_table['equipment'].str.contains(kw)) |
                                  (factory_table['brand'].str.contains(kw)) |
                                  (factory_table['model_short'].str.contains(kw)) |
                                  (factory_table['model'].str.contains(kw)) |
                                  (factory_table['rpm'].str.contains(kw))]
    
    # แปลง DataFrame ที่กรองแล้วเป็นรายการของดิกชันนารี
    data = filtered_data.to_dict('records')

    return render(request, 'employee-search.html', {'form': form, 'data': data})




def my_view(request):
    if request.method == 'POST':
            model = request.POST.get('model')
            fflow = request.POST.get('fflow')
            hhead = request.POST.get('hhead')
            fflow = float(fflow)
            hhead = float(hhead)
            # print(model, type(model))
            # print(fflow, type(fflow))
            # print(hhead, type(hhead))
            if model == 'kdin':
                dfkdin = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table where model_short = "KDIN" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)
                output = [
                loaddata_kdin('FAC-0001', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0002', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0003', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0004', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0005', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0006', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0007', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0008', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0009', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0010', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0011', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0012', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0013', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0014', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0015', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0016', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0017', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0018', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0019', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0020', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0021', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0022', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0023', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0024', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0025', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0026', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0027', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0028', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0029', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0030', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0068', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0069', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0070', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0071', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0072', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0073', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0074', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0075', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0076', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0077', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0078', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0079', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0080', fflow, hhead,dfkdin),
                # # loaddata_kdin('FAC-0081', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0082', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0083', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0084', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0085', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0086', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0087', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0088', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0089', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0090', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0091', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0092', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0093', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0094', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0095', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0096', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0097', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0098', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0099', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0100', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0101', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0102', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0103', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0104', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0105', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0106', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0107', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0108', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0109', fflow, hhead,dfkdin),

                # loaddata_kdin('FAC-0158', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0160', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0161', fflow, hhead,dfkdin),

                # loaddata_kdin('FAC-0164', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0170', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0172', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0174', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0256', fflow, hhead,dfkdin),
                ]

                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]

                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,                    
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead,
                }   
            elif model =='kiso':
                dfkiso = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table where model_short = "KISO" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)
                output = [
                loaddata_kiso('FAC-0031', fflow, hhead,dfkiso),
                loaddata_kiso('FAC-0032', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0033', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0034', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0035', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0036', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0037', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0038', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0039', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0040', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0041', fflow,hhead,dfkiso),
                # loaddata_kiso_two('FAC-0042', fflow,hhead,55,56,30,dfkiso), กราฟ eff ไม่มี
                loaddata_kiso_two('FAC-0043', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0044', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0045', fflow,hhead,dfkiso),
                # loaddata_kiso_two('FAC-0046', fflow,hhead,55,56,30,dfkiso), flow ไม่มี
                loaddata_kiso_two('FAC-0047', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0048', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0049', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0050', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0051', fflow,hhead,dfkiso),
                loaddata_kiso_two("FAC-0052", fflow, hhead, dfkiso),
                loaddata_kiso_two('FAC-0053', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0054', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0055', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0056', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0057', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0058', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0059', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0060', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0061', fflow,hhead,dfkiso),
                # loaddata_kiso('FAC-0062', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0063', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0064', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0065', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0066', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0067', fflow,hhead,dfkiso),
                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            elif model == 'kop9196':
                dfkop9196 = pd.read_sql(f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table where model_short = "KOP9196" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)
                output = [ 
                    loaddata_kop9196('FAC-0110',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0111',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0112',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0114',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0115',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0116',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0117',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0118',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0119',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0120',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0121',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0122',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0123',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0124',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0125',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0126',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0127',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0128',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0129',16,16,dfkop9196), เส้น nhspr ไกลเกิน
                    loaddata_kop9196('FAC-0130',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0131',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0132',fflow,hhead,dfkop9196),  
                    loaddata_kop9196('FAC-0133',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0134',fflow,hhead,dfkop9196), Error Value ***
                    loaddata_kop9196('FAC-0135',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0136',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0137',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0138',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0139',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0140',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0141',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0142',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0143',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0144',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0145',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0146',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0147',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0148',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0149',fflow,hhead,dfkop9196), Error Value ****
                    # loaddata_kop9196('FAC-0150',fflow,hhead,dfkop9196), Error Value ****
                    loaddata_kop9196('FAC-0151',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0152',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0153',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0154',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0155',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0156',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0157',fflow,hhead,dfkop9196),
                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            elif model == 'max3':
                dfmax = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table WHERE model_short LIKE "%MAX%" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)
                output = [ 
                    loaddata_max3('FAC-0159',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0166',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0167',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0175',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0176',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0178',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0179',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0180',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0181',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0182',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0183',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0184',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0185',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0230',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0231',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0232',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0233',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0234',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0235',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0236',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0237',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0238',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0239',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0240',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0241',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0242',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0243',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0244',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0245',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0246',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0247',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0248',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0249',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0250',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0251',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0252',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0253',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0254',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0255',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0229',fflow,hhead,dfmax),
                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            return render(request, 'my_template.html',context)

    else:
        return render(request, 'my_template.html')


def read_table(request):
    data_table = pd.read_sql('SELECT fac_number, equipment, brand, model_short, model, rpm FROM factory_table GROUP BY fac_number' , con=mydb)
    
    return render(request, 'table.html', {'data_table': data_table})

# def show_details(request, fac_number):
#     # ดึงข้อมูลจากฐานข้อมูลตาม fac_number
#     factory = pd.read_sql(f'SELECT fac_number, equipment, brand, model_short, model, rpm FROM factory_table  WHERE fac_number = "{fac_number}"', con=mydb)

#     # ส่งข้อมูลไปยังเทมเพลตสำหรับแสดงรายละเอียด
#     return render(request, 'details.html', {'factory': factory})
def show_details(request, fac_number):
    # sql = f"SELECT * FROM factory_table WHERE fac_number = '{fac_number}'"
    factory = pd.read_sql(f"SELECT fac_number,model_short,data_type,rpm,imp_dia,flow,head,eff,npshr,kw,model FROM factory_table WHERE fac_number = '{fac_number}' ", con=mydb)

    factory.fillna('', inplace=True)
    # หากไม่มีข้อมูล ส่งข้อความแจ้งเตือนกลับไปยังเทมเพลต
    return render(request, 'details.html', {'factory': factory})


def index(request):
    return render(request, 'index.html')




# im_size_lst, flow_list, head_list, eff_size_lst, eff_flow_list, eff_head_list, flow_input, Head_input, name












































































