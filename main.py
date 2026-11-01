class Node:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class OrganizationTree:
    def __init__(self, root_node):
        self.root = root_node

    def search_node(self, query, current_node=None):
        if current_node is None:
            current_node = self.root

        if query.lower() in current_node.jabatan.lower() or (current_node.nama and query.lower() in current_node.nama.lower()):
            return current_node

        for child in current_node.children:
            result = self.search_node(query, child)
            if result:
                return result
        return None

    def insert_node(self, parent_jabatan, child_node):
        parent = self.search_node(parent_jabatan)
        if parent:
            parent.add_child(child_node)
            return True
        print(f"Gagal: Atasan dengan jabatan '{parent_jabatan}' tidak ditemukan.")
        return False

    def preorder_traversal(self, node=None, depth=0):
        if node is None:
            node = self.root
        print("  " * depth + f"- {node.jabatan}")
        for child in node.children:
            self.preorder_traversal(child, depth + 1)

    def inorder_traversal(self, node=None, depth=0):
        if node is None:
            node = self.root
        if node.children:
            self.inorder_traversal(node.children[0], depth + 1)
        print("  " * depth + f"- {node.jabatan}")
        for child in node.children[1:]:
            self.inorder_traversal(child, depth + 1)

    def postorder_traversal(self, node=None, depth=0):
        if node is None:
            node = self.root
        for child in node.children:
            self.postorder_traversal(child, depth + 1)
        print("  " * depth + f"- {node.jabatan}")


# ==========================================
# INISIALISASI DATA SESUAI GAMBAR SKENARIO
# ==========================================
if __name__ == "__main__":
    # Root
    tree = OrganizationTree(Node("-", "Rektor (Root)"))

    # Level 1
    tree.insert_node("Rektor (Root)", Node("-", "Senat Universitas"))
    tree.insert_node("Rektor (Root)", Node("-", "Wakil Rektor I (Bidang Akademik)"))
    tree.insert_node("Rektor (Root)", Node("-", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)"))
    tree.insert_node("Rektor (Root)", Node("-", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)"))
    tree.insert_node("Rektor (Root)", Node("-", "Dekan Fakultas Sains dan Teknologi"))

    # Level 2 (Bawahan Dekan FST)
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("-", "Wakil Dekan I (Bidang Akademik & Kelembagaan)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("-", "Wakil Dekan II (Bidang AUPK)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("-", "Wakil Dekan III (Bidang Kemahasiswaan)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", Node("-", "Ketua Program Studi Teknik Informatika"))

    # Level 3 (Bawahan Ketua Prodi)
    tree.insert_node("Ketua Program Studi Teknik Informatika", Node("-", "Sekretaris Program Studi"))
    tree.insert_node("Ketua Program Studi Teknik Informatika", Node("-", "Kepala Laboratorium Komputer"))
    tree.insert_node("Ketua Program Studi Teknik Informatika", Node("-", "Koordinator Dosen"))

    # Level 4 (Bawahan Kalab & Koor)
    tree.insert_node("Kepala Laboratorium Komputer", Node("-", "Asisten Laboratorium"))
    tree.insert_node("Kepala Laboratorium Komputer", Node("-", "Teknisi Laboratorium"))
    tree.insert_node("Koordinator Dosen", Node("-", "Dosen Pembimbing Akademik"))
    tree.insert_node("Koordinator Dosen", Node("-", "Dosen Pengampu Mata Kuliah"))

    # Level 5 (Bawahan DPA)
    tree.insert_node("Dosen Pembimbing Akademik", Node("-", "Mahasiswa Bimbingan (Leaf)"))

    print("\n--- HASIL PRE-ORDER TRAVERSAL ---")
    tree.preorder_traversal()
    
    print("\n--- HASIL IN-ORDER TRAVERSAL ---")
    tree.inorder_traversal()
    
    print("\n--- HASIL POST-ORDER TRAVERSAL ---")
    tree.postorder_traversal()