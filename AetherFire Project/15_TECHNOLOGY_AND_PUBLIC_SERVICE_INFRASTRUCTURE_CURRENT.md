# AetherFire — Technology & Public-Service Infrastructure Current Canon

> Module ID: `AFM-010`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Shared technology/service interfaces, removable personal terminal, Guest Pass, prepaid wallet, device deposit, and device lifecycle.
> Authority boundary: Controls the accepted general-terminal and guest-service model; does not establish universal deployment, a single backend, agency ownership, or unresolved implementation details.
> Cross-domain owner boundary: Global institutions and geopolitics are controlled by `AFM-001`; legal/civic status and shared economic namespaces by `AFM-002`; Undie professions, occupational hardware and Undi by `AFM-003`; detailed aviation and RF airspace by `AFM-008`.
> Load mode: `FULL_FILE`

> **Integration:** 2026-10-03; user-approved selective admission after audit AF-NEW-001–008.
> **Sources:** the four 2026-10-02/03 inputs recorded in `91_RECONCILIATION_RECORD.md`; original proposal/history wording is provenance, not authority over this accepted view.
> **Truth boundary:** the functional architecture below is accepted canon/design direction. Implementation, scale and present rollout remain `UNKNOWN` where unspecified; genealogy does not establish present capabilities.

## 1. Nền công nghệ và ranh giới miền

AetherFire dùng engineering để cưỡng ép compatibility giữa magic và technology. Hội đồng Pháp sư là actor quan trọng; quan hệ thể chế thuộc `10`. Hàng không ổn định, theo lịch và có thể scale là bằng chứng trực tiếp về năng lực tổ chức trong miền hàng không, do `80` kiểm soát; không suy mọi ngành hoặc địa phương có cùng năng lực.

Các capability định danh, xác thực, thanh toán, dữ liệu, bảo trì và dịch vụ có thể được sử dụng qua giao diện chung. Giao diện tương tác không chứng minh một database, một chủ sở hữu, một cơ quan quản trị hay mức phổ cập toàn quốc. Không dùng độ trưởng thành của một hệ chuyên dụng để áp thứ bậc bắt buộc giữa công nghệ nghề nghiệp, dân dụng và chiến lược. Nguồn năng lượng, sản xuất, chi phí và chuỗi cung ứng chưa được xác lập.

## 2. Chuyển giao công nghệ, không chuyển giao địa vị hoặc cưỡng chế

Undie là nguồn gốc thiết kế công nghệ giao diện, không phải mẫu ontology/policy cho khách. Năng lực terminal, mail/user information, retina có thành phần tích hợp cơ thể, audio tích hợp xương tai, commission forum và gọi an ninh khẩn cấp có điều kiện vẫn là năng lực đã chốt. Retcon 2026-10-05 ở `30` bỏ collar/dấu cơ thể bắt buộc và quyền liên lạc theo Pink/rank; không suy mọi người hành nghề mới phải cấy ghép hoặc chịu quyền lệnh cũ.

Chuyển giao công nghệ không nhập đồ thị rank, Credit Score/Line đã nghỉ hưu, workline, quyền lệnh, hạn chế di chuyển hay cưỡng chế vào terminal khách hoặc vào mặc định nghề Undie mới. Payment/retail, blacklist và AI safety của collar lịch sử chưa được phục hồi thành chức năng collar hiện hành. Nanofabric/self-repair/first-aid của Undi cũng chỉ là genealogy.

## 3. Personal Terminal — kiến trúc chức năng

Personal Terminal là thiết bị cá nhân gắn trên cơ thể nhưng tháo rời được, làm giao diện tới định danh, access, thanh toán và dịch vụ; không phải một smartphone thu nhỏ.

```text
Personal Terminal = Terminal Core + compatible Body Dock
Terminal ≠ identity source of truth ≠ legal status ≠ account ≠ access authority
Shared interface ≠ shared database ≠ shared authority
```

Core chứa xử lý, credential an toàn, liên lạc và giao diện dịch vụ/thanh toán/hiển thị riêng. Core chuyển giữa các mount tương thích; wrist device/bracelet là ví dụ, không phải hình thức duy nhất đã chốt. Credential nối với backend liên quan, không tự tạo quyền pháp lý.

### 3.1 Giữ thiết bị, chống giật và tháo an toàn

- Người đeo hợp lệ có thể xác thực để mở khóa và tháo bình thường; phương thức xác thực còn mở.
- Unexpected detachment/cutting/snatching làm khóa credential của thiết bị, chức năng thanh toán/access trên thiết bị và khả năng đọc thông tin riêng.
- Khi bị mắc vào máy móc/phương tiện hoặc lực nguy hiểm vượt ngưỡng an toàn, Body Dock breakaway và credential khóa. Ngưỡng chưa chốt; chống trộm không được biến thiết bị thành vật trói giữ cơ thể.

Khóa/revoke thiết bị không đồng nghĩa xóa số dư ví, thay đổi legal status hay tước quyền rời đi. Cách tiếp tục xác thực, truy cập dịch vụ và khôi phục quyền sau sự cố vẫn `UNKNOWN`.

### 3.2 Giao diện riêng và theo ngữ cảnh

Hướng thiết kế chấp nhận private retina interface và private audio không cưỡng chế. Giao diện có thể phục vụ định danh, navigation, số dư, xác nhận giao dịch, quyền truy cập, tin nhắn và thông báo dịch vụ/khẩn cấp.

**Chưa chốt cơ chế chuyển từ năng lực retina/bone-integrated audio đã xác lập sang thiết bị khách tháo rời.** Không mặc định khách phải cấy ghép, hoặc đã có một giải pháp không xâm lấn; thành phần cơ thể, đồng thuận, vô hiệu hóa khi tháo/trả/mất và liên kết thiết bị vẫn mở.

Terminal ưu tiên ngữ cảnh: transit ở cổng, mua hàng ở vending, định danh/access ở checkpoint, giấy tờ/thủ tục ở nơi cung cấp dịch vụ. Đây là thiết kế AetherFire được chấp nhận tại đây, không nhập ontology, quyền hạn hay implementation từ The Kingdom POT.

## 4. Guest Pass và quy trình cấp

Guest Pass gồm credential định danh tạm thời, access profile tạm thời, service profile và giao diện tới Guest Wallet. Nó không phải legal status/class mới, không đồng nghĩa Citizen/Civil và không tự cấp quyền nhập cảnh/cư trú.

```text
foreign visitor → identity verification → Guest Profile
→ device deposit collected → Guest Terminal issued
→ Guest Pass bound to terminal → Guest Wallet activated
```

Terminal có guest mode với credential/validity/access profile, ví trả trước và hồ sơ đặt cọc riêng. Thẩm quyền cấp, điều kiện nhập cảnh và full access matrix còn mở.

## 5. Ba đối tượng phải tách

| Đối tượng | Chức năng | Không đồng nghĩa |
| --- | --- | --- |
| Device Deposit | Bảo đảm thiết bị; tạo động lực hoàn trả; hoàn khi trả bình thường | Số dư chi tiêu của ví |
| Guest Wallet | Giá trị trả trước cho giao dịch tương thích | Đặt cọc, Credit Score, Credit Line hoặc legal status |
| Access Profile | Quyền truy cập nơi/dịch vụ trong phạm vi được cấp | Tiền, class hoặc social hierarchy |

Guest Wallet dùng tên biến tài chính riêng. AF-OPEN-006 được supersede bởi retcon Undie 2026-10-05, không phải được giải quyết bằng mô hình ví khách. Không phục hồi bare `credit`/cost/bonus theo web cũ; denomination và triển khai ví vẫn mở.

## 6. Đặt cọc và ví

### 6.1 Device Deposit

Hồ sơ gồm guest ID, terminal ID, đồng tiền, số tiền danh nghĩa, nơi/thời gian cấp và refund entitlement. Deposit không chuyển thành giá trị chi tiêu ví. Khi thiết bị được trả bình thường, hoàn đúng số tiền danh nghĩa trong đồng tiền ghi lúc cấp. Con số `500` của nguồn là ví dụ, không phải mức đặt cọc canon.

Quy tắc này tách deposit khỏi quy đổi để chi tiêu; không chứng minh toàn bộ vấn đề ngoại hối/quyết toán đã được giải quyết. Hạ tầng quyết toán và mức đặt cọc theo đồng tiền/quốc gia còn mở.

### 6.2 Guest Wallet

Ví vận hành theo `load value → spend → reload`. Miền sử dụng gồm transit, vending, ordinary retail, thực phẩm/nhu yếu phẩm và dịch vụ được chấp thuận tương thích; QR/tap là giao diện thanh toán. Danh sách này không chứng minh mọi nhà cung cấp đã tham gia hoặc mọi khách có cùng access.

Đơn vị tiền ví và xử lý số dư chưa dùng khi rời đi vẫn `OPEN`. Trả terminal không tự hoàn số dư ví.

## 7. Giao dịch và quyền riêng tư tối thiểu

QR biểu diễn payment request: recipient, amount, transaction reference, expiry và metadata tùy chọn; không chứa tiền lưu trữ có thể chuyển nhượng. Terminal hiển thị riêng người nhận/số tiền/mục đích/hạn; khách xác nhận; payment backend xử lý giao dịch.

Vending công bố dữ liệu sản phẩm/dịch vụ; người dùng chọn và xác nhận qua terminal; backend trả `PAYMENT_OK`; máy cấp hàng. Máy chỉ nhận claims cần thiết như `PAYMENT_OK`, `AGE/ACCESS_OK`, `ITEM_PERMISSION_OK`, không tự nhận toàn bộ identity/status/legal history, Credit Score hoặc Contribution Points. Quy tắc này không tự xác lập luật privacy/data-retention quốc gia.

## 8. Trả thiết bị, hoàn đặt cọc và mất thiết bị

### 8.1 Return Machine

Trong luồng trả bình thường: xác minh terminal ID, nhận thiết bị, đóng Guest Pass session/revoke credential của thiết bị, sanitize local/private data, đưa hardware vào reissue pool và authorize deposit refund.

`Terminal accepted + refund entitlement recorded/authorized` là một giao dịch trả hoàn chỉnh. Không được để máy giữ terminal nhưng mất quyền hoàn đặt cọc. Nếu khâu giao tiền thất bại, claim vẫn khôi phục được qua terminal khác hoặc quầy có nhân viên. Quyền claim không đồng nghĩa đã nhận tiền thành công.

Thứ tự chi tiết giữa trả thiết bị, revoke Guest Pass và hoàn tất exit/checkpoint chưa chốt. Không mặc định khách có thể qua mọi cổng sau revoke; cơ chế xác thực không cần terminal và duy trì quyền đi ra phải được xác định trước khi mô tả quy trình chi tiết là hoàn chỉnh.

### 8.2 Lost/damaged terminal

Báo mất dẫn đến revoke credential thiết bị cũ; thiết bị cũ không còn dùng để thanh toán/access. Có thể cấp thiết bị thay thế và bind lại Guest Profile. Thu deposit mới và giữ deposit cũ theo điều kiện trả thiết bị là **candidate accounting**, không phải chính sách đã chốt. Hạch toán mất/hỏng, số dư ví và phục hồi quyền truy cập còn mở.

## 9. Các mục chưa chốt và thẩm quyền đối chiếu

### AF-TECH-001 — Terminal/Guest Pass implementation: UNKNOWN / OPEN

Giữ đủ 15 nhóm câu hỏi của nguồn Terminal:

1. Hình thức/vật liệu thiết bị.
2. Xác thực người đeo.
3. Retina implementation; liên kết cơ thể, đồng thuận và vô hiệu hóa khi tháo/trả/mất.
4. Private audio implementation và chuyển đổi từ bone-integrated audio.
5. Nguồn năng lượng terminal.
6. Quyết toán foreign currency/AetherFire Credits.
7. Guest Wallet denomination.
8. Xử lý unused balance lúc exit.
9. Lost/damaged-device accounting, deposit cũ/mới và wallet recovery.
10. Full access matrix, admission/legal recognition và xác thực/exit sau mất/trả/revoke.
11. Agencies chịu trách nhiệm identity/payment/access/device lifecycle.
12. Privacy/data-retention law.
13. Offline behavior và service continuity.
14. Mức deposit theo quốc gia/đồng tiền.
15. Quan hệ với future revised Undie hardware.

### AF-TECH-002 — Nền công nghiệp/hạ tầng: UNKNOWN / OPEN

Giữ 15 nhóm của Technology Notes: industrial energy; cơ chế nanotechnology nếu sau này phục hồi; device standards authority; ownership ID/payment network; national data architecture; backend concentration/distribution; privacy/data-rights; cybersecurity; robot/android production scale; automation share; rare-material supply; collar/Undi/aircraft cost; procurement; banking/currency/public finance; civilian/commercial/military/intelligence technology gaps. Việc ghi câu hỏi không chấp nhận nanofabric hay một ngành công nghiệp cụ thể thành canon.

`10` kiểm soát thể chế; `20` kiểm soát status và economic namespaces; `30` kiểm soát nghề Undie, phần cứng nghề còn mở và Undi; `80` kiểm soát aviation. Các unknown hiện có trong những miền này vẫn có hiệu lực; module này không thay quyền sở hữu nội bộ của chúng.
