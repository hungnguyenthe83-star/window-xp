import streamlit as st

# Cấu hình giao diện mở rộng tối đa của Streamlit
st.set_page_config(page_title="Microsoft Windows XP", page_icon="💾", layout="wide")

# Bộ code HTML/CSS/JS giả lập chính xác cấu trúc Windows XP
html_xp_perfect = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Windows XP Professional</title>
    <style>
        body {
            margin: 0; padding: 0; overflow: hidden;
            font-family: 'Tahoma', 'Segoe UI', sans-serif;
            user-select: none;
            background: #0051e6;
        }
        /* Màn hình Desktop với ảnh nền Bliss gốc độ phân giải cao */
        #desktop {
            width: 100vw; height: 560px;
            background: url('https://unsplash.com') center/cover no-repeat;
            position: relative;
            box-sizing: border-box;
            padding: 10px;
        }
        
        /* Hệ thống Icon chuẩn cổ điển */
        .desktop-icon {
            width: 75px; height: 75px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            cursor: pointer; text-align: center; margin-bottom: 12px;
            border: 1px solid transparent; border-radius: 2px;
        }
        .desktop-icon:hover {
            background: rgba(43, 114, 245, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .desktop-icon span {
            color: white; font-size: 11px; margin-top: 4px;
            text-shadow: 1px 1px 1px rgba(0,0,0,0.9);
            font-family: 'Tahoma';
        }
        .icon-img {
            width: 32px; height: 32px;
            background-size: contain; background-repeat: no-repeat;
        }
        /* Link ảnh icon WinXP thật */
        .img-computer { background-image: url('https://alexmeub.com'); }
        .img-ie { background-image: url('https://alexmeub.com'); }
        .img-trash { background-image: url('https://alexmeub.com'); }

        /* CỬA SỔ WINDOWS XP CHUẨN ĐẾN TỪNG CHI TIẾT */
        .window {
            position: absolute; width: 450px; height: 320px;
            background: #F1EEE4; border: 3px solid #0054E3;
            border-top-left-radius: 8px; border-top-right-radius: 8px;
            box-shadow: 3px 3px 10px rgba(0,0,0,0.4);
            display: none; flex-direction: column; z-index: 10;
        }
        /* Thanh tiêu đề dốc màu xanh lượn sóng */
        .title-bar {
            background: linear-gradient(to bottom, #0058e6 0%, #0073ea 12%, #0058e6 88%, #0044b3 100%);
            height: 28px; display: flex; align-items: center; justify-content: space-between;
            padding: 0 8px; color: white; font-weight: bold; font-size: 12px;
            text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
            border-top-left-radius: 5px; border-top-right-radius: 5px;
        }
        .title-text { display: flex; align-items: center; gap: 5px; }
        .window-buttons { display: flex; gap: 3px; }
        
        /* 3 Nút bấm huyền thoại góc phải */
        .win-btn {
            width: 21px; height: 21px; border-radius: 3px; cursor: pointer;
            font-weight: bold; font-size: 11px; display: flex; align-items: center; justify-content: center;
            color: white; border: 1px solid rgba(0,0,0,0.4);
        }
        .btn-min { background: linear-gradient(to bottom, #2d7af4, #004cb3); }
        .btn-max { background: linear-gradient(to bottom, #2d7af4, #004cb3); }
        .btn-close {
            background: linear-gradient(to bottom, #e76043 0%, #e74322 15%, #b32d14 100%);
            border-color: #7c1a0c; font-size: 13px;
        }
        .win-btn:hover { filter: brightness(1.2); }
        
        /* Nội thất cửa sổ và thanh Menu bar cổ điển */
        .menu-bar {
            background: #F1EEE4; border-bottom: 1px solid #D2CFBB;
            padding: 3px 10px; font-size: 11px; color: #000; display: flex; gap: 12px;
        }
        .menu-item:hover { background: #316AC5; color: white; cursor: pointer; }
        .window-content {
            padding: 12px; flex-grow: 1; overflow: auto;
            font-size: 12px; color: #000; background: #FFF; margin: 4px;
            border: 1px solid #7F9DB9;
        }

        /* THANH TASKBAR PHÍA DƯỚI */
        #taskbar {
            width: 100vw; height: 40px;
            background: linear-gradient(to bottom, #245edb 0%, #3f8cf3 9%, #245edb 18%, #1b4ca3 100%);
            position: absolute; bottom: 0; left: 0;
            display: flex; align-items: center; justify-content: space-between; z-index: 100;
            border-top: 1px solid #174291;
        }
        
        /* Nút Start màu xanh lá lượn sóng */
        #start-btn {
            background: linear-gradient(to bottom, #388e3c 0%, #5cb85c 10%, #388e3c 90%, #225e25 100%);
            height: 100%; padding: 0 22px; display: flex; align-items: center; gap: 6px;
            color: white; font-weight: bold; font-style: italic; font-size: 16px;
            cursor: pointer; border-top-right-radius: 8px; border-bottom-right-radius: 8px;
            box-shadow: 2px 0 5px rgba(0,0,0,0.4); border: none;
            text-shadow: 1px 1px 1px #114013;
        }
        #start-btn img { width: 18px; }
        #start-btn:hover { filter: brightness(1.15); }

        /* BẢNG START MENU THẬT KHI BẤM NÚT START */
        #start-menu {
            position: absolute; bottom: 40px; left: 0; width: 380px; height: 450px;
            background: #FFF; border: 2px solid #0054E3; border-top-right-radius: 5px;
            box-shadow: 5px -5px 15px rgba(0,0,0,0.5); display: none; z-index: 200;
            flex-direction: column;
        }
        .start-menu-header {
            background: linear-gradient(to bottom, #1c5ae3 0%, #4487f7 100%);
            height: 50px; display: flex; align-items: center; padding: 0 15px;
            color: white; font-weight: bold; font-size: 14px; gap: 10px;
        }
        .start-menu-header img { width: 32px; height: 32px; border: 2px solid #fff; border-radius: 4px; }
        .start-menu-body { display: flex; flex-grow: 1; height: calc(100% - 100px); }
        .start-left { width: 55%; background: #FFF; padding: 10px; display: flex; flex-direction: column; gap: 8px; }
        .start-right { width: 45%; background: #CBDAF4; border-left: 1px solid #99B4E3; padding: 10px; display: flex; flex-direction: column; gap: 10px; font-size: 11px; }
        .start-item { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 4px; font-size: 11px; color:#000;}
        .start-item:hover { background: #316AC5; color: white; }
        .start-menu-footer {
            background: linear-gradient(to bottom, #4487f7 0%, #1c5ae3 100%);
            height: 45px; display: flex; justify-content: flex-end; align-items: center; padding: 0 15px; gap: 15px;
        }
        .logoff-btn { background: #ff9800; border: 1px solid #fff; color: white; padding: 4px 10px; font-weight: bold; cursor: pointer; font-size: 11px; }

        /* Khay hệ thống góc phải màu xanh nước biển */
        #system-tray {
            background: linear-gradient(to bottom, #0c8df6 0%, #1ea1fc 9%, #0c8df6 18%, #045cb4 100%);
            height: 100%; padding: 0 12px; display: flex; align-items: center;
            color: white; font-size: 11px; border-left: 1px solid #084c8c; gap: 10px;
        }
    </style>
</head>
<body>

    <div id="desktop">
        <!-- Hệ thống Icons -->
        <div class="desktop-icon" onclick="openWindow('my-computer')">
            <div class="icon-img img-computer"></div>
            <span>My Computer</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('internet-explorer')">
            <div class="icon-img img-ie"></div>
            <span>Internet Explorer</span>
        </div>
        <div class="desktop-icon" onclick="alert('Thùng rác đang trống!')">
            <div class="icon-img img-trash"></div>
            <span>Recycle Bin</span>
        </div>

        <!-- BẢNG START MENU -->
        <div id="start-menu">
            <div class="start-menu-header">
                <img src="https://alexmeub.com">
                <span>Administrator</span>
            </div>
            <div class="start-menu-body">
                <div class="start-left">
                    <div class="start-item" onclick="openWindow('internet-explorer'); toggleStartMenu();">
                        <img src="https://alexmeub.com" width="24">
                        <strong>Internet Explorer</strong>
                    </div>
                    <div class="start-item" onclick="alert('Đang mở Windows Media Player...'); toggleStartMenu();">
                        <img src="https://alexmeub.com" width="24">
                        <span>Windows Media Player</span>
                    </div>
                </div>
                <div class="start-right">
                    <div class="start-item" onclick="openWindow('my-computer'); toggleStartMenu();" style="font-weight:bold;">My Computer</div>
                    <div class="start-item" onclick="alert('Đang vào Control Panel...')">Control Panel</div>
                    <div class="start-item" onclick="alert('Đang mở trợ giúp...')">Help and Support</div>
                </div>
            </div>
            <div class="start-menu-footer">
                <button class="logoff-btn" onclick="location.reload()">Turn Off Computer 🔴</button>
            </div>
        </div>

        <!-- CỬA SỔ MY COMPUTER CHUẨN GỐC -->
        <div class="window" id="my-computer" style="left: 120px; top: 60px;">
            <div class="title-bar">
                <div class="title-text">

