Update CL và CD thời gian thực dùng matplotlib


mở WSL Ubuntu Terminal lên, navigate vào thư mục chứa file mesh và file configuration của SU2


mở realTimeAeroCoeffsUpdate.py lên, sửa tên file config theo ý muốn (default: config.cfg)


mở file config.cfg lên, sửa/thêm vào:


`SCREEN_OUTPUT=(INNER_ITER, LIFT, DRAG)`


HISTORY_OUTPUT=(INNER_ITER, LIFT, DRAG)`


chạy `./realTimeAeroCoeffsUpdate.py`


enjoy :D
