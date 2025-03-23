import streamlit as st
import random
import pandas as pd 
import time

st.header("Python 🐍 Project")
st.write("Created by Feasible")

tab1, tab2 = st.tabs(["เป่ายิงฉุบ", "อาหารตามสั่ง"])
with tab1:
    st.subheader("Rock Paper Scissors ✊🖐️✌️")
    st.write("Can you beat a computer at Rock-Paper-Scissors?")
    
    if "click_count" not in st.session_state:
        st.session_state.click_count = 0
        st.session_state.pym = ""
        st.session_state.win = 0
        st.session_state.loss = 0
        st.session_state.tie = 0

    left, middle, right = st.columns(3)
    if left.button("✊ Rock", use_container_width=True):
        st.session_state.click_count += 1
        st.session_state.pym = "Rock"
    if middle.button("🖐️ Paper", use_container_width=True):
        st.session_state.click_count += 1
        st.session_state.pym = "Paper"
    if right.button("✌️ Scissors", use_container_width=True):
        st.session_state.click_count += 1
        st.session_state.pym = "Scissors"

    if st.button("Reset / New Game"):

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Win", st.session_state.win)
        col2.metric("Loss", st.session_state.loss)
        col3.metric("Tie", st.session_state.tie)
        col4.metric("Rounds", st.session_state.click_count)

        st.session_state.click_count = 0
        st.session_state.pym = ""
        st.session_state.win = 0
        st.session_state.loss = 0
        st.session_state.tie = 0
        

    if st.session_state.click_count != 0:
        my_list = ["Rock", "Paper", "Scissors"]

        if st.session_state.click_count == 0:
            random_choice = ""
        else:
            random_choice = random.choice(my_list)

        player_choice = st.session_state.pym


        com_p = "https://feasibleth.com/wp-content/uploads/2025/03/Paper.png"
        com_r = "https://feasibleth.com/wp-content/uploads/2025/03/Rock.png"
        com_s = "https://feasibleth.com/wp-content/uploads/2025/03/Scissors.png"

        ply_p = "https://feasibleth.com/wp-content/uploads/2025/03/Paper-R.png"
        ply_r = "https://feasibleth.com/wp-content/uploads/2025/03/Rock-R.png"
        ply_s = "https://feasibleth.com/wp-content/uploads/2025/03/Scissors-R.png"

        if random_choice == "":
            img_comp = None
        elif random_choice == "Rock":
            img_comp = com_r
        elif random_choice == "Paper":
            img_comp = com_p
        elif random_choice == "Scissors":
            img_comp = com_s

        if player_choice == "":
            img_play = None
        elif player_choice == "Rock":
            img_play = ply_r
        elif player_choice == "Paper":
            img_play = ply_p
        elif player_choice == "Scissors":
            img_play = ply_s

        # st.write(f"Computer_move => {random_choice}")  # ผลลัพธ์ที่ได้จะแตกต่างกันไปในแต่ละครั้งที่รัน
        # st.write(f"Player_move => {player_choice}") # ผลลัพธ์จากการเลือกของผู้เล่นแต่ละครั้ง

        # if loop เฉพาะ tie กับ loss นอกนั้น win
        if (player_choice == "" and random_choice == ""):
            None
        elif (player_choice == random_choice):
            txt = "- Tie 😁 -"
            st.session_state.tie += 1
        elif (player_choice == 'Rock' and random_choice == 'Paper'):
            txt = "- You Loss 😭 -"
            st.session_state.loss += 1
        elif (player_choice == 'Paper' and random_choice == 'Scissors'):
            txt = "- You Loss 😭 -"
            st.session_state.loss += 1
        elif (player_choice == 'Scissors' and random_choice == 'Rock'):
            txt = "- You Loss 😭 -"
            st.session_state.loss += 1
        else:
            txt = "- You Win 😎 -"
            st.session_state.win += 1

        lf_, com_, ply_, rf_ = st.columns(4)
        lf_.metric("Round", st.session_state.click_count)
        lf_.metric("Tie", st.session_state.tie)
        com_.image(img_comp, caption="Computer Move")
        ply_.image(img_play, caption="Your Move")
        rf_.metric("Win", st.session_state.win)
        rf_.metric("Loss", st.session_state.loss)

        xx, yy, zz = st.columns(3)
        xx.write("")
        yy.metric("this round", txt)
        zz.write("")

    ## streamlit run TEST02_StreamLit.py

with tab2:
    data = {
        "cate": ["1","1","1","1","1","2","2","2","2","2","3","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","6","7","7","7","8","8","8","8","8"],
        "number": ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
                "31","32","33","34","35","36"],
        "menu": [
            "ผัดกะเพราหมูสับ", "ผัดกะเพราหมูเด้ง", "ผัดกะเพราไข่เยี่ยวม้าหมูสับ", "ผัดกะเพราเครื่องในไก่", "ผัดกะเพรากุนเชียง", 
            "ผัดพริกแกงหมู", "ผัดพริกแกงเนื้อ", "ผัดพริกแกงปลาดุกกรอบ", "ผัดพริกแกงทะเล", "ผัดพริกแกงปลาหมึก", 
            "ผัดคะน้าหมูกรอบ", "ผัดคะน้าปลาเค็ม", "ผัดแขนงหมูกรอบ", "ผัดผักบุ้งไฟแดง", "ผัดยอดฟักแม้ว", 
            "ผัดผงกะหรี่ปลาหมึก", "ผัดผงกะหรี่กุ้ง", "ผัดผงกะหรี่ไก่", "ผัดผงกะหรี่หมู", 
            "หมูสับคั่วพริกกระเทียม", "หมูทอดกระเทียมพริกไทย", "กุ้งกระเทียมพริกไทย", "ไก่กระเทียม", 
            "ยำหมูยอ", "ยำปลากระป๋อง", "ยำวุ้นเส้นโบราณ", "ยำวุ้นเส้นทะเล", "ยำไข่แดงเค็ม", 
            "ข้าวต้มกุ้ง", "ข้าวต้มหมูสับ", "ข้าวต้มปลา", 
            "สุกี้น้ำหมู", "สุกี้น้ำทะเล", "สุกี้แห้งหมู", "สุกี้น้ำไก่", "สุกี้แห้งไก่"
        ],
        "price": [
            50, 55, 65, 55, 60, 50, 65, 80, 70, 60, 55, 55, 55, 50, 50, 65, 65, 50, 50, 50, 50, 80, 50, 50, 50, 65, 65, 50, 40, 40, 50, 50, 50, 50, 50, 50
        ],
        "img": [
            "https://placehold.co/500x500/EEE/31343C?text=Krapow1", "https://placehold.co/500x500/EEE/31343C?text=Krapow2",
            "https://placehold.co/500x500/EEE/31343C?text=Krapow3", "https://placehold.co/500x500/EEE/31343C?text=Krapow4",
            "https://placehold.co/500x500/EEE/31343C?text=Krapow5", "https://placehold.co/500x500/EEE/31343C?text=PrikGang1",
            "https://placehold.co/500x500/EEE/31343C?text=PrikGang2", "https://placehold.co/500x500/EEE/31343C?text=PrikGang3",
            "https://placehold.co/500x500/EEE/31343C?text=PrikGang4", "https://placehold.co/500x500/EEE/31343C?text=PrikGang5",
            "https://placehold.co/500x500/EEE/31343C?text=Kana1", "https://placehold.co/500x500/EEE/31343C?text=Kana2",
            "https://placehold.co/500x500/EEE/31343C?text=Kana3", "https://placehold.co/500x500/EEE/31343C?text=PakBung",
            "https://placehold.co/500x500/EEE/31343C?text=FakMaew", "https://placehold.co/500x500/EEE/31343C?text=PongKaree1",
            "https://placehold.co/500x500/EEE/31343C?text=PongKaree2", "https://placehold.co/500x500/EEE/31343C?text=PongKaree3",
            "https://placehold.co/500x500/EEE/31343C?text=PongKaree4", "https://placehold.co/500x500/EEE/31343C?text=Kratiem1",
            "https://placehold.co/500x500/EEE/31343C?text=Kratiem2", "https://placehold.co/500x500/EEE/31343C?text=Kratiem3",
            "https://placehold.co/500x500/EEE/31343C?text=Kratiem4", "https://placehold.co/500x500/EEE/31343C?text=Yum1",
            "https://placehold.co/500x500/EEE/31343C?text=Yum2", "https://placehold.co/500x500/EEE/31343C?text=Yum3",
            "https://placehold.co/500x500/EEE/31343C?text=Yum4", "https://placehold.co/500x500/EEE/31343C?text=Yum5",
            "https://placehold.co/500x500/EEE/31343C?text=KhaoTom1", "https://placehold.co/500x500/EEE/31343C?text=KhaoTom2",
            "https://placehold.co/500x500/EEE/31343C?text=KhaoTom3", "https://placehold.co/500x500/EEE/31343C?text=Suki1",
            "https://placehold.co/500x500/EEE/31343C?text=Suki2", "https://placehold.co/500x500/EEE/31343C?text=Suki3",
            "https://placehold.co/500x500/EEE/31343C?text=Suki4", "https://placehold.co/500x500/EEE/31343C?text=Suki5"
        ],
        "order": [
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False
        ],
    }

    # ฟังก์ชันสำหรับรีเซ็ต state และแสดงผลใหม่
    def reset_and_display():
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()  # ใช้หรือไม่ก็ได้แล้วแต่ Streamlit version

    # Initial state
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(data)
        st.session_state.customer_name = ""
        st.session_state.order_placed = False
        st.session_state.selected_a_df = pd.DataFrame()
        st.session_state.selected_b_df = pd.DataFrame()
        st.session_state.selected_c_df = pd.DataFrame()
        st.session_state.selected_d_df = pd.DataFrame()
        st.session_state.selected_e_df = pd.DataFrame()
        st.session_state.selected_f_df = pd.DataFrame()
        st.session_state.selected_g_df = pd.DataFrame()
        st.session_state.selected_h_df = pd.DataFrame()

    # ---- เริ่มโค้ด ส่วนแสดงผล ---------------------------------------
    my_shop = "ตั้งหวังเจ๊งโภชนา"

    st.subheader(f"""ยินดีต้อนรับสู่ {my_shop}""")
    st.markdown("**:red[สูตรเด็ดพี่ชาย คายตั้งแต่คำแรก]**")

    customer_name = st.text_input("กรุณาแจ้งชื่อของคุณลูกค้าครับ:", key="customer_name")
    if len(customer_name) > 0:
        st.write("สวัสดีครับ คุณ ", customer_name, "สั่งอาหารอะไรดีครับ?")

        taba, tabb, tabc, tabd, tabe, tabf, tabg, tabh = st.tabs(["ผัดกะเพรา", "ผัดพริกแกง", "ผัดผัก", "ผัดผงกะหรี่", 
                                                                    "ผัดกระเทียม", "ยำ", "ข้าวต้ม", "สุกี้"])
        with taba:
            df_a = st.session_state.df[st.session_state.df['cate'] == "1"].copy()
            df_a = df_a.drop(['cate'], axis='columns')
            config = {
                # "cate": st.column_config.TextColumn("Category"),
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            # สร้าง st.data_editor
            st.session_state.selected_a_df = st.data_editor(df_a, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="taba_editor")
        with tabb:
            df_b = st.session_state.df[st.session_state.df['cate'] == "2"].copy()
            df_b = df_b.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_b_df = st.data_editor(df_b, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabb_editor")
        with tabc:
            df_c = st.session_state.df[st.session_state.df['cate'] == "3"].copy()
            df_c = df_c.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_c_df = st.data_editor(df_c, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabc_editor")
        with tabd:
            df_d = st.session_state.df[st.session_state.df['cate'] == "4"].copy()
            df_d = df_d.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_d_df = st.data_editor(df_d, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabd_editor")
        with tabe:
            df_e = st.session_state.df[st.session_state.df['cate'] == "5"].copy()
            df_e = df_e.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_e_df = st.data_editor(df_e, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabe_editor")
        with tabf:
            df_f = st.session_state.df[st.session_state.df['cate'] == "6"].copy()
            df_f = df_f.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_f_df = st.data_editor(df_f, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabf_editor")
        with tabg:
            df_g = st.session_state.df[st.session_state.df['cate'] == "7"].copy()
            df_g = df_g.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_g_df = st.data_editor(df_g, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabg_editor")
        with tabh:
            df_h = st.session_state.df[st.session_state.df['cate'] == "8"].copy()
            df_h = df_h.drop(['cate'], axis='columns')
            config = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร", width="large"),
                "price": st.column_config.NumberColumn("ราคา (฿)", width="small"),
                "img": st.column_config.ImageColumn("รูปประกอบ"),
                "order": st.column_config.CheckboxColumn("สั่งเลย?", help = "ติ๊กเลือก **รายการ** เพื่อสั่ง", default = False)
            }
            st.session_state.selected_h_df = st.data_editor(df_h, column_config=config,
                                                            disabled=["number", "menu", "price", "img"],
                                                            hide_index=True, key="tabh_editor")
            
        # รวมรายการทุกแท็บ
        all_selected_df = pd.concat([st.session_state.selected_a_df, st.session_state.selected_b_df, st.session_state.selected_c_df,
                                        st.session_state.selected_d_df, st.session_state.selected_e_df, st.session_state.selected_f_df,
                                        st.session_state.selected_g_df, st.session_state.selected_h_df], ignore_index=True)

        # กรองรายการที่ถูกเลือก
        selected_items_df = all_selected_df[all_selected_df['order']]
        selected_items_df = selected_items_df.drop(['img', 'order'], axis='columns')
        sum_total = selected_items_df['price'].sum()
        cnt_total = selected_items_df['number'].count()

        # แสดงรายการที่ถูกเลือก
        if not selected_items_df.empty:
            st.write("รายการอาหารที่เลือก:")
            config_a = {
                "number": st.column_config.TextColumn("เลขที่"),
                "menu": st.column_config.TextColumn("รายการอาหาร"),
                "price": st.column_config.NumberColumn("ราคา (฿)"),
            }

            col_a, col_b = st.columns(2)
            with col_a:
                st.dataframe(selected_items_df, column_config=config_a, hide_index=True)
            with col_b:
                st.metric(label="จำนวนรายการที่สั่ง", value=cnt_total)
                st.metric(label="คิดเป็นยอดรวมทั้งหมด", value=sum_total)
            st.session_state.order_placed = True
        else:
            st.write("กรุณาเลือกรายการอาหาร")
        
        # เพิ่มปุ่ม "ชำระเงิน"
        if st.button("ชำระเงิน", type="primary", disabled=not st.session_state.order_placed):
            st.write("ขอบคุณสำหรับการสั่งอาหาร!")  # แสดงข้อความขอบคุณ
            with st.spinner("Wait for it..."):
                time.sleep(2)
            st.success("Done!")
            reset_and_display()  # เรียกฟังก์ชันรีเซ็ตเมื่อกดปุ่ม
            

