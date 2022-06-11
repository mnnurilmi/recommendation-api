
# Recommender API

API for recommending videos based on watch history of a user

## API Reference

### Get Recommendation Based on Watch History

#### Route
```http
  POST /api/v1/inference
```
#### Request Example
```json
{
  "user_request": ["string"],
  "ids": [21,22,23,25,25,26,27,28,29,210]
}
```
#### Response Example
```json
[
  {
        "description": "FROZEN FOOD MODAL KECIL! OWNERNYA MASIH KECIL OMSET 130JUTA PERBULAN ...",
        "genre": "Kuliner|Review",
        "id": "reeDm_UdZPY",
        "thumbnail": "https://i.ytimg.com/vi/reeDm_UdZPY/mqdefault.jpg",
        "title": "FROZEN FOOD MODAL KECIL! OWNERNYA IMUT, OMSETNYA130JUTA PERBULAN (2021)"
    },
    {
        "description": "Bisnis yang lagi hits dimasa pandemi frozen food nuget ekonomis dari 1/4 daging ayam jadi 7 pack isi 10 pcs dengan modal ...",
        "genre": "Kuliner|Tutorial|Review",
        "id": "xOJiNBjx8zg",
        "thumbnail": "https://i.ytimg.com/vi/xOJiNBjx8zg/mqdefault.jpg",
        "title": "Ide bisnis frozen food ekonomis modal 20K jual 70K bisnis (2021)"
    },
    {
        "description": "Halooo Assalammualaikum ...Siapa disini yang udah kangen dengan video rekomendasi supplier tangan pertama selanjutnya ...",
        "genre": "Homecare|Ecommerce",
        "id": "Quv46YQcKNo",
        "thumbnail": "https://i.ytimg.com/vi/Quv46YQcKNo/mqdefault.jpg",
        "title": "5 REKOMENDASI SUPPLIER TANGAN PERTAMA PERABOTAN RUMAH TANGGA TERMURAH DAN TERBESAR DI SHOPEE (2021)"
    },
    {
        "description": "Panggilan untuk Insinyur Indonesia.",
        "genre": "Healthcare|Tutorial|Review",
        "id": "wxDve0kLZBM",
        "thumbnail": "https://i.ytimg.com/vi/wxDve0kLZBM/mqdefault.jpg",
        "title": "Produksi Masker Massal Dari China | Mesin Pembuat Masker Otomatis (2021)"
    },
    {
        "description": "Assalammualaikum Wr.Wb.. Salam sejahtera buat sahabat semua. Dalam video ini menayangkan toko perabotan rumah tangga ...",
        "genre": "Homecare",
        "id": "yEmjvg7NsZ8",
        "thumbnail": "https://i.ytimg.com/vi/yEmjvg7NsZ8/mqdefault.jpg",
        "title": "Toko Alat Perabotan Rumah Tangga Lengkap Di Cirebon (2021)"
    },
    {
        "description": "lagi marak masker di indonesia karena wabah covid-19 , anda jelas tidak mau beli masker yg abal abal kan ? monggo disimak ...",
        "genre": "Healthcare|Review",
        "id": "EavT9P1y3xk",
        "thumbnail": "https://i.ytimg.com/vi/EavT9P1y3xk/mqdefault.jpg",
        "title": "Review Masker Beckoning import (2021)"
    },
    {
        "description": "Hai guys, ga bs bahasa cina, beli di yoybuy ditranslate pake bahasa indonesia/english WWW.1688.COM WWW.YOYBUY.",
        "genre": "Homecare",
        "id": "d9DVOppPcXM",
        "thumbnail": "https://i.ytimg.com/vi/d9DVOppPcXM/mqdefault.jpg",
        "title": "IDE BISNIS IMPORT PERALATAN DAPUR BELI GROSIR DI 1688.COM (2021)"
    },
    {
        "description": "Di video ini saya membicarakan kerangka belajar digital marketing untuk pemula. Ada 3 fase yang Anda perlu pahami yaitu: Build ...",
        "genre": "Tutorial|Ecommerce|Marketing",
        "id": "gGAA5gxzRoE",
        "thumbnail": "https://i.ytimg.com/vi/gGAA5gxzRoE/mqdefault.jpg",
        "title": "Kerangka Ideal Belajar Digital Marketing Untuk Pemula (2021)"
    },
    {
        "description": "LEBIH ENAK DARI KENTUCKY�?����BISA DI JADIIN IDE BISNIS FROZEN FOOD Assalammualaikum bosquee Semoga selalu ...",
        "genre": "Kuliner|Tutorial",
        "id": "875pyraIHbU",
        "thumbnail": "https://i.ytimg.com/vi/875pyraIHbU/mqdefault.jpg",
        "title": "LEBIH ENAK DARI KENTUCKY�?�??�?Ǭ��BISA DI JADIIN IDE BISNIS FROZEN FOOD (2021)"
    },
    {
        "description": "Banyak dropshipper yang bingung cara mencari supplier tangan pertama yang benar. Kebanyakan dapat supplier yang diluar ...",
        "genre": "Kuliner|Homecare|Healthcare|Tutorial|Ecommerce",
        "id": "mrZ6hldg2tw",
        "thumbnail": "https://i.ytimg.com/vi/mrZ6hldg2tw/mqdefault.jpg",
        "title": "Cara Mencari Supplier Tangan Pertama Untuk Reseller Dropship (2021)"
    }
]
```
#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

