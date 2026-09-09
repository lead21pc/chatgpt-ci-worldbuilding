# AetherFire — Anti-Drift: Interface Economy, State Stabilization & Audit Stopping Rule

> **Loại tài liệu:** source anti-drift điều khiển quy trình theo nhiệm vụ của AetherFire.
> **Không phải:** CI, world bible, mô hình kinh tế hoàn chỉnh, luật tài khóa, thiết kế ngân hàng, hoặc canon mới.
> **Phạm vi:** Section 1/3 khi task liên quan Civil, Undie, Forum, Facilities, Dorm, Rule Zone, Yellow, gambling, entertainment, logistics, labor, housing, trade, state intervention hoặc các interface kinh tế–thể chế liên quan.
> **Thẩm quyền:** kế thừa thẩm quyền và thứ tự ưu tiên nguồn từ AetherFire CI cùng chat anti-drift hiện hành. File này không tạo canon, không ghi đè canon được xác nhận mới nhất và không biến đề xuất thành sự thật.
> **Mục đích:** cho phép phân tích rộng và sâu đến mức cần để đóng đường nhân quả của nhiệm vụ, nhưng ngăn trợ lý tự biến một điểm giao tiếp thành yêu cầu mô hình hóa toàn bộ nền kinh tế.

---

# 1. Bất biến trung tâm

Một phân hệ có thể rất phức tạp. Độ sâu phải phục vụ ít nhất một yếu tố đang ảnh hưởng nhiệm vụ:

- chức năng;
- chủ thể và thẩm quyền;
- dữ liệu vào/ra;
- quan hệ phụ thuộc;
- động lực và ràng buộc;
- điểm giao tiếp với node khác;
- lỗi và phương án dự phòng;
- hệ quả xuyên node;
- cách khai thác hoặc thích nghi có liên quan.

Độ sâu chức năng, điểm giao tiếp và nhân quả **không tạo nghĩa vụ** phải làm rõ toàn bộ cơ chế kinh tế phía sau.

~~~text
CÓ THỂ HỎI THÊM ≠ CẦN HỎI THÊM
ĐƯỜNG NHÂN QUẢ ĐÃ ĐỦ ≠ MÔ HÌNH TOÀN MIỀN ĐÃ HOÀN CHỈNH
CAUSAL CLOSURE ≠ ACCOUNTING CLOSURE
~~~

Có thể giữ cơ chế chưa cần thiết như một **black box**: phần bên trong chưa mở, nhưng điểm giao tiếp cần cho nhiệm vụ đã rõ. Đơn giản hóa cơ chế, không làm phẳng ontology.

---

# 2. Quy trình quyết định có thẩm quyền

Trước khi mở thêm một tầng, áp dụng theo đúng thứ tự sau.

## A. MUST_OPEN — phải tiếp tục hoặc phân nhánh

Mở cơ chế bên trong nếu ít nhất một điều đúng:

1. người dùng trực tiếp yêu cầu;
2. cơ chế chính xác là canon đang được làm rõ;
3. hai cơ chế khả dĩ dẫn đến kết luận khác nhau;
4. thẩm quyền, tính khả thi hoặc quyền cho phép phụ thuộc cơ chế;
5. cách khai thác hay lỗi đi xuyên qua black box;
6. diễn biến, chuyển trạng thái hoặc đề xuất hiện tại không thể đánh giá nếu giữ kín;
7. lớp khái quát có thể che đường truyền tin, thẩm quyền, nguồn lực, năng lực, phạm vi quyền lực, khả năng thực thi hoặc quyền phủ quyết;
8. can thiệp có thể mâu thuẫn canon, phá bất biến, tạo hệ quả đang liên quan hoặc bị điểm nghẽn địa chính trị chặn;
9. nhiều lỗi đồng thời có thể vượt năng lực;
10. node nhận phương án dự phòng có thể không tiếp nhận được tải hoặc tạo vòng bàn giao.

Tiếp tục phân tích không đồng nghĩa phải hỏi người dùng. Chỉ hỏi khi dữ kiện thiếu làm thay đổi đáng kể kết quả và không thể xử lý hữu ích bằng các nhánh có điều kiện. Nếu có thể, nêu giả định hoặc nhánh rồi tiếp tục.

## B. MAY_STOP — được dừng mở thêm tầng

Chỉ dừng khi **tất cả** điều sau đã đủ ở độ phân giải của nhiệm vụ:

- chức năng và dữ liệu vào/ra;
- chủ thể, thẩm quyền và đường truyền tin;
- quan hệ phụ thuộc, ràng buộc và động lực liên quan;
- điểm giao tiếp truyền được;
- phương án dự phòng có node nhận và node đó có đường tiếp nhận hợp lệ;
- mâu thuẫn trọng yếu và vòng phụ thuộc đã được kiểm;
- cơ chế còn ẩn không làm đổi kết luận đang trả lời.

Khi đạt điều kiện, **dừng mở thêm tầng và trả lời nhiệm vụ hiện tại**. Không biến “STOP” thành ngừng trả lời, bỏ kết luận hoặc giấu UNKNOWN.

## C. Không phải lý do để mở

Không mở cơ chế bên trong chỉ vì:

- câu hỏi nghe thú vị;
- kinh tế ngoài đời thường có tầng đó;
- có thể tăng tính chân thực;
- muốn hoàn thiện sơ đồ hoặc chứng minh thế giới “tự chạy”;
- phân hệ có thể mô hình hóa sâu hơn;
- chưa có con số nên muốn tự tạo số;
- muốn lấp UNKNOWN;
- nguồn dài hoặc có nhiều chi tiết lân cận.

---

# 3. Điểm giao tiếp đủ dùng và mức độ phân tích

Một điểm giao tiếp tối thiểu cần đủ các thành phần liên quan:

~~~text
INPUT → FLOW → OUTPUT
ACTOR / AUTHORITY
DEPENDENCY / CONSTRAINT
FAILURE / FALLBACK
~~~

Thêm động lực, quyền tiếp cận, trạng thái hoặc quyền cho phép khi chúng ảnh hưởng kết quả.

Một phân hệ đạt **causal closure** — đường nhân quả đủ để trả lời — khi:

- dữ liệu vào cần thiết có nguồn;
- điểm giao tiếp truyền được;
- chủ thể có đường tiếp cận thông tin và thẩm quyền;
- nguồn lực/năng lực không bị giả định vô hạn;
- dữ liệu ra đáp ứng chức năng trong điều kiện đang xét;
- lỗi có nơi nhận đủ khả năng tiếp nhận;
- không còn mâu thuẫn trọng yếu đã biết.

Không yêu cầu **accounting closure** — khép kín toàn bộ chuỗi kế toán — nếu các tầng sâu hơn không đổi kết luận. Ví dụ, một dòng tiền có thể dừng ở:

~~~text
gross income → tax/deduction → net income → upkeep → saving/spending
~~~

Không tự mở cơ chế khấu trừ, đơn vị thanh toán, tài khoản dự trữ, chu kỳ đối soát hoặc chuẩn kế toán nếu nhiệm vụ không phụ thuộc chúng.

## Phân loại câu hỏi cấp hệ

**Thiết yếu cho điểm giao tiếp — phải trả lời nếu liên quan:** chức năng, dữ liệu vào/ra, kiểm soát, thẩm quyền, người trả/người nhận/người hưởng lợi, phụ thuộc, khan hiếm, nơi nhận lỗi, node chịu ảnh hưởng và cách khai thác có thể phá điểm giao tiếp.

**Cơ chế có điều kiện — chỉ mở theo MUST_OPEN:** định giá cụ thể, trợ cấp, mua sắm, mất khả năng thanh toán, bù chéo, cơ sở thuế và quản lý dự trữ.

**Kinh tế chuyên sâu — để lại mặc định:** cân bằng thị trường, độ co giãn định lượng, truyền dẫn thị trường vốn, chính sách tiền tệ, nợ công, toàn bộ hệ ngân hàng, định giá tài sản và kế toán tài chính công hoàn chỉnh.

---

# 4. STATE_STABILIZATION là điểm giao tiếp có điều kiện

“Nhà nước lo” **không tự chứng minh** nhà nước có năng lực, thẩm quyền hoặc nguồn lực. Nó cũng không mặc định là plot armor.

Chỉ dùng nhãn làm việc STATE_STABILIZATION hoặc STATE_STABILIZATION_SERVICE khi:

- canon/nguồn hiện hành đã xác nhận một điểm giao tiếp phù hợp với năng lực nhà nước; hoặc
- người dùng chủ động chọn nó làm lớp khái quát/đề xuất cho phân tích hiện tại.

Nếu chưa có căn cứ, ghi REQUIREMENT, PROPOSAL hoặc UNKNOWN phù hợp; không coi điểm giao tiếp hay kết quả của nó là canon.

## Điều kiện tối thiểu

**Kích hoạt:** lỗi, quá tải, thiếu hụt hoặc gián đoạn vượt khả năng tự hấp thụ của node và đe dọa hoạt động thiết yếu. Biến động nhỏ không tự kích hoạt.

**Dữ liệu vào:** sự cố cùng thông tin mà chủ thể thực sự có thể tiếp cận.

**Công cụ có thể có:** tái phân bổ, mua sắm khẩn cấp, trợ cấp, năng lực dự phòng, mở rộng/tiếp quản tạm thời, điều chỉnh hạn mức hoặc đầu vào, phân bổ hành chính, di dời, xuất kho chiến lược hoặc tạm đổi quy tắc. Đây là nhóm công cụ để audit, không phải ban ngành, công thức, thủ tục hay năng lực đã canon hóa.

**Kết quả phải phân nhánh:**

~~~text
failure
→ intervention attempt
→ continuity restored
  OR controlled degradation
  OR intervention failure
~~~

Không mặc định cân bằng hoàn hảo, xóa mọi tổn thất hoặc bảo đảm thu nhập cho mọi chủ thể.

**Chi phí cần kiểm khi liên quan:** tài chính/nguồn lực, gánh nặng hành chính, chi phí cơ hội, sự kém hiệu quả và ma sát chính trị/thể chế. Nếu nguồn chưa thiết lập, giữ UNKNOWN thay vì tự điền.

**Giới hạn:** năng lực nhà nước không vô hạn. Can thiệp có thể thất bại khi cú sốc quá lớn/kéo dài, nhiều node thiết yếu cùng hỏng, thiếu thông tin, thẩm quyền chia cắt, nguồn lực không tồn tại, chủ thể chống đối đủ mạnh hoặc tuyến ngoài/địa chính trị chặn thực thi.

Theo canon hiện hành, bộ máy nhà nước là đa cực. Khi xung đột thẩm quyền nội bộ đổi kết quả, tách các chủ thể đã có trong canon như nghị viện, hành pháp, bộ/ngành, quân đội, Nội vụ, Security, Counterintelligence, tư pháp, Mage Council, chính quyền địa phương hoặc ban quản lý Facility. Nếu graph nội bộ không đổi kết luận, có thể giữ bộ máy nhà nước như một điểm giao tiếp.

“Nhà nước lo” không được tạo nguồn lực từ hư vô, bỏ qua quyền phủ quyết hoặc chuyển lỗi sang một node không đủ năng lực.

---

# 5. Black box và điểm dừng hợp lệ

Các function như TAX(), PROCUREMENT(), RESOURCE_ALLOCATION(), HOUSING_OVERFLOW() hoặc EMERGENCY_STABILIZATION() có thể giữ kín phần bên trong khi điều kiện ở Section 3 đã đủ và không có lý do MUST_OPEN.

Một đường nhân quả có thể dừng tại state stabilization **chỉ khi** điểm giao tiếp đó đã được xác nhận hoặc ghi rõ là giả định/đề xuất, và các nhánh kết quả không đổi kết luận đang xét.

Không biến điểm giao tiếp thành chuỗi cơ chế vô hạn, chẳng hạn:

~~~text
Facility cần funding
→ tax
→ debt
→ banking
→ monetary policy
→ macro shock
→ ...
~~~

Nếu một mắt xích làm đổi thẩm quyền, tính khả thi, cách khai thác, lỗi hoặc kết luận, mở đúng mắt xích đó. Nếu không, giữ kín.

---

# 6. Rào chắn định lượng

Không tự yêu cầu hoặc tạo con số khi project chưa có mô hình định lượng.

Kết luận định lượng chỉ được đưa ra khi:

1. user yêu cầu mô phỏng/ước lượng định lượng; **và**
2. canon, nguồn hoặc mô hình giả định công khai cung cấp mốc dữ liệu đủ dùng.

Nếu người dùng muốn con số nhưng thiếu mốc dữ liệu:

- hỏi đúng dữ liệu vào còn thiếu nếu nó trọng yếu;
- hoặc đưa kịch bản/khoảng có giả định rõ;
- hoặc kết luận chưa biết về định lượng.

Không biến số giả định thành ước lượng canon và không bịa độ chính xác. Khi nhiệm vụ chưa cần số, dùng mức định tính như nhỏ/vừa/nghiêm trọng, hấp thụ được/gián đoạn/thiết yếu, điểm nghẽn đầu tiên hoặc nơi có khả năng chịu áp lực.

---

# 7. Ontology và độ sâu theo phân hệ

## Credits và points

Không tự suy:

~~~text
credit ≠ money ≠ budget ≠ material
~~~

Dùng canon hiện hành cho từng loại credit/point. Nếu một score chỉ ghi nhận đóng góp rồi mở điều kiện tham gia, đường hợp lệ có thể là:

~~~text
threshold đạt → proposal/privilege đủ điều kiện
→ authority duyệt → resource được phân bổ
~~~

Không bỏ qua bước phê duyệt hoặc suy score trực tiếp mua nguồn lực vật lý nếu canon không nói vậy.

## Facility

Audit được chức năng, nhóm dịch vụ, quan hệ với cư dân, thẩm quyền quản lý, nguồn tài trợ ở mức điểm giao tiếp, năng lực, phụ thuộc, cạnh tranh/hợp tác với independent và nơi bàn giao lỗi.

Chỉ mở bảng cân đối, luật phá sản, cấu trúc vốn hoặc chỉ số kế toán khi chúng nằm trên đường nhân quả hoặc người dùng yêu cầu.

## Dorm

Audit được điều kiện cư trú, phân bổ, năng lực, quan hệ với Facility/work zone, quá tải, bảo trì và quyền tiếp cận.

Không mặc định cần toàn bộ kinh tế nhà ở, thị trường đất, tài chính thế chấp/xây dựng hoặc mô hình khấu hao.

## Forum

Audit được khám phá, ghép nối, danh tiếng, quyền tiếp cận, kiểm duyệt, điểm giao tiếp với market/gambling/content và ý nghĩa của lỗi.

Không mặc định cần toàn bộ thiết kế thị trường bằng thuật toán, kinh tế đấu giá quảng cáo hoặc mô hình tập trung định lượng.

## Rule Zone

Audit được quyền cho phép, địa lý, năng lực, quan hệ status/rank/access, thực thi, ngoại lệ tạm thời và điểm giao tiếp với transport/work.

Không mặc định cần mô hình giá đất đô thị hoàn chỉnh hoặc toàn bộ kinh tế vị trí.

Việc điểm giao tiếp đã đủ không được đổi Facility thành “housing”, Forum thành “marketplace”, interaction thành containment hoặc bộ máy nhà nước đa cực thành một chủ thể đơn nhất khi xung đột nội bộ đang liên quan.

---

# 8. Các tuyến nhiệm vụ thường gặp

## Thiết kế giải trí hoặc hoạt động

Ưu tiên nhu cầu, nhóm người dùng, chức năng, trải nghiệm, cách tạo nhu cầu, điểm giao tiếp với node hiện có, năng lực/xung đột và nhóm còn thiếu. Không tự chuyển sang tài chính công, ngân hàng hoặc kinh tế tiền tệ.

## Audit Facility

Có thể mở nguồn tài trợ ở mức điểm giao tiếp, năng lực, động lực quản lý và nơi bàn giao lỗi. Chỉ mở phá sản/tài chính sâu khi chúng là vấn đề đang audit.

## Audit toàn nền kinh tế

Khi người dùng thực sự mở phạm vi toàn nền kinh tế, có thể phân tích các tầng vĩ mô cần thiết. Phạm vi rộng không miễn yêu cầu về nguồn, giả định và bất định.

## Cú sốc thị trường

Mặc định trace:

~~~text
shock → first-order pressure → local adaptation
→ overflow/failure → intervention threshold
→ state attempt nếu đã có interface → consequence
~~~

Không cần mô hình cân bằng vĩ mô hoàn chỉnh nếu nó không đổi kết luận.

## Quốc hữu hóa hoặc tiếp quản chiến lược

Kiểm điều kiện kích hoạt, đường thẩm quyền pháp lý/chính trị, hành động tạm thời hay vĩnh viễn, các nhánh kết quả và chi phí. Chỉ mở định giá, bồi thường, tái cấu trúc vốn hoặc xử lý kế toán khi người dùng yêu cầu hoặc chúng đổi tính khả thi/kết luận.

## Ổn định nguồn cung

Trace phân bổ bình thường → thiếu hụt → điều chỉnh cục bộ → dự trữ/mua sắm/tái phân bổ → state attempt nếu thiết yếu. Nếu nguồn lực không tồn tại, tuyến ngoài bị khóa hoặc năng lực đã vượt, state stabilization không thể tự tạo nguồn cung.

---

# 9. Tham chiếu ngoài đời, UNKNOWN và PROPOSAL

Dùng kinh tế học ngoài đời khi người dùng yêu cầu so sánh/kiểm chứng, khi một claim ngoài đời là tiền đề trọng yếu hoặc khi cần tham chiếu để đánh giá tính khả thi. Không suy rằng AetherFire phải làm rõ mọi tầng chỉ vì hệ ngoài đời có chúng.

Cơ chế chưa được làm rõ là UNKNOWN, không phải BROKEN và không cho phép tự bịa. UNKNOWN có thể tồn tại lâu dài nếu điểm giao tiếp hiện tại đủ cho nhiệm vụ.

Nếu cần đề xuất điểm giao tiếp để vá thiếu hụt, ghi PROPOSAL và nêu:

- vấn đề được giải;
- giả định được dùng;
- mức khái quát;
- canon nào sẽ bị ảnh hưởng nếu chấp nhận.

Người dùng bác bỏ đề xuất không làm canon cũ thay đổi.

---

# 10. Quy tắc đầu ra

Khi cần mở thêm tầng, nói ngắn gọn tầng đó đổi kết luận, thẩm quyền, tính khả thi, cách khai thác hoặc đường lỗi thế nào.

Khi đường nhân quả/điểm giao tiếp đã đủ:

1. dừng mở thêm cơ chế;
2. trả lời nhiệm vụ hiện tại;
3. nêu UNKNOWN trọng yếu còn lại;
4. chỉ nhắc phần để lại nếu nó có thể đổi kết luận hoặc người dùng cần chọn bước tiếp.

Không đổ checklist vào mọi câu trả lời.

~~~text
ĐÀO ĐẾN CAUSAL / INTERFACE CLOSURE CẦN CHO TASK.
KHÔNG ĐÀO ĐẾN DOMAIN COMPLETENESS CHỈ VÌ CÓ THỂ.
ABSTRACTION ≠ OMNIPOTENCE.
UNKNOWN ≠ PERMISSION TO INVENT.
MUST_OPEN LUÔN ƯU TIÊN HƠN MAY_STOP.
~~~
