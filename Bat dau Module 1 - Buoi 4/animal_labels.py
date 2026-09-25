file_names = [
    "cat_001.jpg",
    "dog_001.jpg",
    "cat_002.jpg",
    "bengal_tiger_001.jpg",
    "dog_002.jpg",
    "bengal_tiger_002.jpg",
]


def extract_label(file_name):
    # TODO: Tra ve nhan loai tu ten file.
    # Vi du: "bengal_tiger_001.jpg" -> "bengal_tiger"
    pass


def extract_labels(names):
    # TODO: Tra ve list cac nhan va khong thay doi names.
    pass


def find_unique_labels(names):
    # TODO: Tra ve set cac nhan khong trung lap.
    pass


def count_labels(names):
    # TODO: Tra ve dict theo dang {label: so_lan_xuat_hien}.
    pass


# Bat dau viet test case cua ban o day.
# assert extract_label("cat_001.jpg") == "cat"
# assert extract_label("bengal_tiger_001.jpg") == "bengal_tiger"


# Chi bo comment khi cac ham da duoc hoan thien.
# print(count_labels(file_names))
