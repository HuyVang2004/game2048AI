# game2048AI

### Thuật toán sử dụng Expectiminimax
![MinhHoa](https://algomaths.tech/wp-content/uploads/2020/12/expectimaximin.png)
  - Tại mỗi trạng thái cụ thể duyệt hết tất cả các hướng đi của trạng thái đó (lên, xuống, trái, phải)
  - Nếu độ sâu tìm kiếm bằng 0 hoặc trạng thái đó là trạng thái kết thúc của trò chơi thì sẽ trả về giá trị của trạng thái đó (cần một hàm đánh giá giá trị của từng trạng thái)
  - Nếu trạng thái là MAX thì gọi đệ quy hàm expectiminimax để tìm giá trị Max của các trạng thái con (thực hiện di chuyển trang thái hiện tại theo các hướng và giảm độ sau tìm kiếm đi 1)
  - Nếu trạng thái là CHANCE thì tính trung bình tất cả các giá trị của các trạng thái có thể sinh ra
      $$score = \frac{1}{n} \sum_{i = 1}^{n} evaluate_i * p_i$$
          Trong đó: $evaluate_i$$là giá trị trạng thái i                        
                $p_i$ là xác suất xuất hiện trạng thái đó                       
                $n$ là số vị trí trống

### Đánh giá giá trị cho từng trạng thái
- Cố gắng đẩy các số lớn về vị trị các góc. Có 8 đường đi để làm điều đó
  ![Đườngdẫn](https://github.com/HuyVang2004/game2048AI/blob/main/images/Screenshot%202023-12-02%20192514.png?raw=true)
- Tính giá trị trạng thái cụ thể = giá trị lớn nhất của trạng thái đó trong 8 đường dẫn
- Các tính tại mỗi đường dẫn $$evaluate = \sum_{i = 0}^{n - 1} value_i * 2 ^ i$$
    trong đó $value_i$ là giá trị tại vị trí i trong đường dẫn
