![Tiếng Việt dùng nhiều hơn 35% token so với tiếng Anh trong GPT](/token-tieng-viet-gpt-vi.jpg)

Tôi dịch cùng một prompt chăm sóc khách hàng sang 41 ngôn ngữ và đếm token bằng o200k_base, tokenizer hiện tại của OpenAI (GPT-4o trở về sau). Tiếng Anh cần 34 token, tiếng Việt **46 token — nhiều hơn 35%**, đứng thứ 15/41 (1 = rẻ nhất).

Bản tiếng Việt:

> Hãy tóm tắt email của khách hàng dưới đây thành ba ý chính và đề xuất một câu trả lời lịch sự. Khách hàng nói rằng đơn hàng đến trễ hai ngày và thiếu một món trong hộp.

## Kết quả

| Ngôn ngữ | Token | So với tiếng Anh | Tiết kiệm nếu gửi bằng tiếng Anh |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| **Tiếng Việt** | **46** | **+35%** | **26%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Biểu đồ: số token tăng thêm của từng ngôn ngữ so với tiếng Anh trong GPT (41 ngôn ngữ)](/blog-language-tax-chart-v5.png)

## Vì sao

![Vì sao: Khách → Kh | ách · 2; Hãy → H | ãy · 2; tóm → t | óm · 2](/token-tieng-viet-gpt-vi-sao-vi.jpg)

Tokenizer học chủ yếu từ văn bản tiếng Anh: những từ như " polite" hay " customer" chỉ là một token, còn chữ tiếng Việt có dấu thường bị tách ra:

- Khách → `Kh | ách` · 2
- Hãy → `H | ãy` · 2
- tóm → `t | óm` · 2

## Chuyển sang tiếng Anh chỉ với một nút bấm

Cách tiết kiệm nhiều nhất là gửi prompt bằng tiếng Anh: ít hơn khoảng 26% token so với tiếng Việt. Các mô hình hiện nay hiểu chỉ dẫn tiếng Anh rất tốt và sẽ trả lời bằng tiếng Việt nếu bạn yêu cầu. Trong [công cụ đếm token TokenSave](/vi/), hãy dán prompt và bấm **💸 Tiết kiệm token**: nó dọn khoảng trắng, dịch sang tiếng Anh, lược bỏ phần thừa và thêm "Reply in Vietnamese." để câu trả lời vẫn bằng ngôn ngữ của bạn. Tính năng dùng trình dịch tích hợp trong Chrome 138+ / Edge 148+ trên máy tính; việc dịch chạy trên thiết bị của bạn và văn bản không bao giờ bị tải lên. Bấm **↩ Bản gốc** để lấy lại bản gốc.

## Quy ra tiền

Với mô hình giá 2 $ cho 1 triệu token đầu vào, gửi prompt này 1 triệu lần tốn 68 $ bằng tiếng Anh và 92 $ bằng tiếng Việt. Nếu câu trả lời cũng bằng tiếng Việt, hệ số này áp dụng cả cho token đầu ra, vốn thường đắt hơn 300–400%.

## Cách tiết kiệm

![Cách tiết kiệm: Viết system prompt và hướng dẫn cố định bằng tiếng Anh; chỉ giữ tiếng Việt cho phần người dùng nhập.; Yêu cầu ](/token-tieng-viet-gpt-cach-tiet-kiem-vi.jpg)

- Viết system prompt và hướng dẫn cố định bằng tiếng Anh; chỉ giữ tiếng Việt cho phần người dùng nhập.
- Yêu cầu các bước trung gian (phân loại, trích xuất, gọi công cụ) bằng tiếng Anh hoặc JSON, chỉ câu trả lời cuối bằng tiếng Việt.
- Dùng prompt caching cho phần cố định của prompt.

## Giới hạn

- Chỉ đo một prompt; với văn bản khác tỉ lệ có thể lệch ±0,1–0,2.
- Claude và Gemini dùng tokenizer khác; các con số chỉ đúng với mô hình OpenAI.
- Bản dịch dựa trên dịch máy đã được kiểm tra.

Kết quả đầy đủ 41 ngôn ngữ (tiếng Anh): [so sánh 41 ngôn ngữ](/blog/token-cost-by-language)

Xem cả 41 ngôn ngữ cạnh nhau trong [bảng ngôn ngữ](/languages).

## Nguồn

- [tiktoken: bộ tách token của OpenAI (o200k_base) trên GitHub](https://github.com/openai/tiktoken)
- [Bảng giá OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
