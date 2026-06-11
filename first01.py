import math

def print_header(title):
    """ฟังก์ชันสำหรับแสดงหัวข้อเมนูให้สวยงาม"""
    print("\n" + "="*50)
    print(f" {title} ".center(50, "*"))
    print("="*50)

def get_positive_float(prompt):
    """ฟังก์ชันสำหรับรับค่าตัวเลขที่มากกว่า 0 และป้องกันข้อผิดพลาด"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ ข้อผิดพลาด: ค่าต้องมากกว่า 0 กรุณากรอกใหม่อีกครั้ง")
                continue
            return value
        except ValueError:
            print("❌ ข้อผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")

def calculate_rectangle():
    print_header("โปรแกรมคำนวณพื้นที่สี่เหลี่ยมมุมฉาก")
    width = get_positive_float("📐 กรุณากรอกความกว้าง: ")
    length = get_positive_float("📐 กรุณากรอกความยาว: ")
    area = width * length
    print(f"\n✅ ผลลัพธ์: พื้นที่สี่เหลี่ยมมุมฉากคือ {area:,.2f} ตารางหน่วย")

def calculate_triangle():
    print_header("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")
    base = get_positive_float("📐 กรุณากรอกความยาวฐาน: ")
    height = get_positive_float("📐 กรุณากรอกความสูง: ")
    area = 0.5 * base * height
    print(f"\n✅ ผลลัพธ์: พื้นที่สามเหลี่ยมคือ {area:,.2f} ตารางหน่วย")

def calculate_circle():
    print_header("โปรแกรมคำนวณพื้นที่วงกลม")
    radius = get_positive_float("📐 กรุณากรอกรัศมีของวงกลม (r): ")
    area = math.pi * (radius ** 2)
    print(f"\n✅ ผลลัพธ์: พื้นที่วงกลมคือ {area:,.2f} ตารางหน่วย")

def main():
    while True:
        print("\n" + "="*50)
        print("   โปรแกรมคำนวณพื้นที่รูปทรงเรขาคณิต [เวอร์ชันพัฒนาต่อยอด]   ")
        print("="*50)
        print(" 1. คำนวณพื้นที่สี่เหลี่ยมมุมฉาก (จากต้นแบบ)")
        print(" 2. คำนวณพื้นที่สามเหลี่ยม (เพิ่มความสามารถใหม่)")
        print(" 3. คำนวณพื้นที่วงกลม (เพิ่มความสามารถใหม่)")
        print(" 4. ออกจากโปรแกรม")
        print("="*50)
        
        choice = input("👉 กรุณาเลือกเมนู (1-4): ").strip()
        
        if choice == "1":
            calculate_rectangle()
        elif choice == "2":
            calculate_triangle()
        elif choice == "3":
            calculate_circle()
        elif choice == "4":
            print("\n🎉 ขอบคุณที่ใช้งานโปรแกรมของเรา! สวัสดีค่ะ/ครับ 🎉\n")
            break
        else:
            print("❌ เมนูไม่ถูกต้อง! กรุณาเลือกหมายเลข 1-4 เท่านั้น")

if __name__ == "__main__":
    main()
