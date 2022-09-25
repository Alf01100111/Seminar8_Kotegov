import hb_functions as f
import handbook_base as hb
import gui as g

def button_click():
    handbook_temp = hb.get_base()

    hb.get_storage(f.new_data(f.new_id(f.read_base(handbook_temp)), g.get_surname(), g.get_name(), g.get_phone_num()))
    
    # print(f.find(g.get_surname(), f.read_base(handbook_temp)))

    hb.del_data()