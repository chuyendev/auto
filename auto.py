import subprocess
import time

def run_adb_command(command):
    """Hàm chạy lệnh ADB."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Lỗi khi chạy lệnh: {e}")
        return None

def open_tiktok():
    """Mở ứng dụng TikTok."""
    print("Đang mở TikTok...")
    run_adb_command("adb shell monkey -p com.zhiliaoapp.musically -c android.intent.category.LAUNCHER 1")
    time.sleep(5)  # Chờ TikTok mở

def swipe_up():
    """Vuốt lên trên màn hình."""
    print("Vuốt lên...")
    run_adb_command("adb shell input swipe 500 1500 500 500")

def close_tiktok():
    """Tắt ứng dụng TikTok."""
    print("Đang đóng TikTok...")
    run_adb_command("adb shell am force-stop com.zhiliaoapp.musically")

def main():
    """Chương trình chính."""
    try:
        open_tiktok()
        for i in range(3):  # Thực hiện 3 lần
            time.sleep(12)  # Chờ 12 giây
            swipe_up()
        
        close_tiktok()
        print("Hoàn thành, đóng chương trình.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
