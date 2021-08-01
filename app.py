DB_ART_PRODUCTS = [
    {
        "이름" : "붓"
    },
    {
        "이름" : "물감"
    },
    {
        "이름" : "물통"
    },

]

DB_TEST_KIT = [
    {
        "이름" : "비커"
    },
    {
        "이름" : "유리막대"
    },
]

DB_PE_TOOLS = [
    {
        "이름" : "축구공"
    },
    {
        "이름" : "야구배트"
    },
    {
        "이름" : "야구공"
    },
]


def startAS() :
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")
    print("1. 학교물건 리스트")
    print("2. 학교물건 추가")
    print("3. 학교물건 삭제")
    print("4. 프로그렘 종료")
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")

    answer = int(input(">>  "))

    if answer == 1 :
        view_PP()
    elif answer == 2 :
        create_SC()
    elif answer == 3 :
        delete_SC()
    elif answer == 4 :
        print("[SYSTEM] 프로그렘을 종료합니다.")
    else:
        print("[SYSTEM] 잘못 입력했습니다.")
        startAS()








def view_PP() :
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")
    print("1. 미술도구")
    print("2. 실험도구")
    print("3. 체육물품")
    print("4. 뒤로가기")
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")

    answer = int(input(">>  "))


    if answer == 1 :
        AS()
    elif answer == 2 :
        TK()
    elif answer == 3 :
        PET()
    elif answer == 4 :
        startAS()
    else:
        print("[SYSTEM] 잘못 입력했습니다.")
        view_PP()

        
def AS() :
    print("🍀 미술도구 리스트 🍀")
    for ART_PRODUCTS in DB_ART_PRODUCTS :
        print(f"물건 이름 : {ART_PRODUCTS['이름']}")
        print("🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨")
    
    view_PP()

def TK() :
    print("🍀 실험도구 리스트 🍀")
    for TEST_KIT in DB_TEST_KIT :
        print(f"물건 이름 : {TEST_KIT['이름']}")
        print("🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪")
    view_PP()


def PET() :
    print("🍀 체육물품 리스트 🍀")
    for PE_TOOLS in DB_PE_TOOLS :
        print(f"물건 이름 : {PE_TOOLS['이름']}")
        print("💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼💪🏼")

    view_PP()


def create_SC() :
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")
    print("추가할 물건의 종류를 선택해 주세요")
    print("1. 미술도구")
    print("2. 실험도구")
    print("3. 체육물품")
    print("4.뒤로가기")
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")

    answer = int(input(">>  "))

    if answer == 1 :
        create_AS()
    elif answer == 2 :
        create_TK()
    elif answer == 3 :
        create_PET()
    elif answer == 4 :
        startAS()
    else:
        print("[SYSTEM] 잘못 입력했습니다.")
        create_SC()


def create_AS() :

    input_name = input("물건의 이름을 입력해주세요. >>")


    push_data = {
        "이름" : input_name,
    }

    DB_ART_PRODUCTS.append(push_data)

    create_SC()

def create_TK() :

    input_name = input("물건의 이름을 입력해주세요. >>")


    push_data = {
        "이름" : input_name

    }

    DB_TEST_KIT.append(push_data)

    create_SC()

def create_PET() :

    input_name = input("물건의 이름을 입력해주세요. >>")


    push_data = {
        "이름" : input_name

    }

    DB_PE_TOOLS.append(push_data)

    create_SC()

def delete_SC() :
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")
    print("삭제할 물건의 종류를 선택해 주세요")
    print("1. 미술도구")
    print("2. 실험도구")
    print("3. 체육물품")
    print("4.뒤로가기")
    print("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪")

    answer = int(input(">>  "))

    if answer == 1 :
        delete_AS()
    elif answer == 2 :
        delete_TK()
    elif answer == 3 :
        delete_PET()
    elif answer == 4 :
        startAS()
    else:
        print("[SYSTEM] 잘못 입력했습니다.")
        delete_AS()

def delete_AS() :
    for ART_PRODUCTS in enumerate(DB_ART_PRODUCTS) :
        print(f"{ART_PRODUCTS[0]} _ {ART_PRODUCTS[1]['이름']}")
    input_index = int(input("삭제할 데이터의 번호를 입력해주세요."))

    DB_ART_PRODUCTS.pop(input_index)
    print("입력하신 데이터가 삭제되었습니다.")

    delete_SC()

def delete_TK() :
    for TEST_KIT in enumerate(DB_TEST_KIT) :
        print(f"{TEST_KIT[0]} _ {TEST_KIT[1]['이름']}")
    input_index = int(input("삭제할 데이터의 번호를 입력해주세요."))

    DB_TEST_KIT.pop(input_index)
    print("입력하신 데이터가 삭제되었습니다.")

    delete_SC()

def delete_PET() :
    for PE_TOOLS in enumerate(DB_PE_TOOLS) :
        print(f"{PE_TOOLS[0]} _ {PE_TOOLS[1]['이름']}")
    input_index = int(input("삭제할 데이터의 번호를 입력해주세요."))

    DB_PE_TOOLS.pop(input_index)
    print("입력하신 데이터가 삭제되었습니다.")

    delete_SC()








startAS()

