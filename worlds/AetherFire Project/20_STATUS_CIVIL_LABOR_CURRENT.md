# AetherFire — Status, Civil & Labor Current Canon

> Module ID: `AFM-002`
> Runtime role: `CURRENT_SOURCE`
> Domain / Scope: Status ontology, Citizen, Civil, Yellow, POW, Criminal, Civil entry/allocation/lifecycle, labor, and cross-status transitions.
> Authority boundary: Controls legal/civic status ontology and Civil/labor interfaces within its declared scope.
> Cross-domain owner boundary: Detailed Undie professional identity, entry/exit, mobility, work/access, and Undi are controlled by `AFM-003`; shared Terminal/Guest Pass service architecture by `AFM-010` without replacing this module's status and economic-namespace authority.
> Load mode: `FULL_FILE`

> **Domain:** status ontology, social hierarchy, Citizen/Civil/Yellow/POW/Criminal, Civil entry/allocation/lifecycle, cross-status transitions and shared economic/access namespaces.  
> Dedicated Civil law controls its exact scope. The ontology map controls axis separation. Remaining gaps stay `UNKNOWN / UNRESOLVED`.  
> **Retcon — 2026-10-05:** Undie là căn tính/hệ sinh thái nghề nghiệp, không phải địa vị pháp lý hoặc lớp Slave. Đồ thị màu/rank và chuyển địa vị cũ đã nghỉ hưu; `30` kiểm soát luật nghề còn mở. Career Rank ngoài Undie không bị thay thế.

## Part I — Resolved status and ontology map

### Guest-service interface — accepted 2026-10-03

`15_TECHNOLOGY_AND_PUBLIC_SERVICE_INFRASTRUCTURE_CURRENT.md` controls the removable terminal and Guest Pass functional model. Guest Pass is a temporary credential/access/service profile, not a legal status, class, Citizen/Civil conversion, or immigration/residency entitlement. Device Deposit, Guest Wallet and Access Profile remain separate objects; a terminal is not an account or access authority.

Guest Wallet có biến tài chính riêng. Kiến trúc Credit Score/Line và bare `credit` phụ thuộc cơ chế Undie cũ đã bị supersede theo retcon 2026-10-05; AF-OPEN-008 và các unknown triển khai ví vẫn mở. Không dùng ví khách để phục hồi các biến cũ. Guest access, legal recognition and recovery/exit after device loss/return are not inferred from existing Civil or Undie rules; AF-TECH-001 records these unknowns.

### AetherFire — Current Status & Ontology Map

> Chỉ gồm ontology hiện hành đã resolve trong cụm Citizen–Civil–Undie. Mọi khoảng trống được ghi `UNKNOWN`; file này không tạo canon mới.
>
> **Truth-status rule:** `ABSENCE OF CANON ≠ CANONICAL NEGATION`; `NOT ESTABLISHED ≠ FALSE`; hai trục độc lập không tự cho biết các giá trị của chúng có thể kết hợp hoặc ánh xạ thế nào.

#### 1. STATUS

**Definition:** trạng thái pháp lý/civic đang chi phối subject; không đồng nhất với class, job, rank, zone hay economic variable.

**Known values trong phạm vi:**

- `Citizen` — citizen status.
- `Civil Slave` — Slave legal status với civic standing ngang Citizen trong phạm vi đã chốt.
- `Yellow` — trạng thái kỷ luật tạm thời của Citizen, một tuần ở lần đầu rồi trở lại Citizen. Undi không còn là dấu địa vị/trừng phạt mặc định; trang phục của Yellow cần xác nhận riêng.
- `POW` — public status; backend dùng Slave security category nhưng không kéo POW vào Civil/Criminal/Undie ontology.
- `Slave` — phạm trù pháp lý có Civil và Criminal trong phạm vi đã chốt; không chứa Undie.

**Known transitions:**

```text
Citizen
→ accepted real Civil billet + final confirmation
→ Civil Slave

Civil Slave
→ review bắt đầu từ năm 5
→ nếu tới năm 10 chưa được duyệt/xét: Citizen trực tiếp

Citizen → first offense → Yellow → 1 tuần → Citizen
repeat Yellow-rule offense → outcome UNKNOWN [Yellow→Red/Undie đã nghỉ hưu; không tự giữ quota ×2]

death-sentence exposure → plea → Criminal Slave
```

**UNKNOWN:** thời điểm và chế tài tái phạm Yellow; tiêu chí/thẩm quyền/ngoại lệ review Civil năm 5; quyền đơn phương rời Civil. Gia nhập Undie là quan hệ nghề, không tạo conversion hoặc White→Citizen.

#### 1A. SOCIAL HIERARCHY / CIVIC STANDING

Social hierarchy là trục riêng với legal status và class.

```text
Hoàng gia > Quý tộc > Sĩ quan quân đội = POW > Thượng lưu > Trung lưu > Trí thức > Citizen = Civil Slave > Criminal
```

`Citizen = Civil Slave` chỉ ở civic standing/social tier, không phải legal-status identity. Undie không còn là một bậc cố định của hierarchy hoặc social caste; nghề không tự quyết định giá trị xã hội. Vị trí Purple/Hazel theo đồ thị cũ không còn dùng được.

#### 2. CLASS / COLOR

##### Class

- `Civil Slave` — source xác nhận đây là legal status/labor line; exact separate class-field label không được tự suy.
- `Undie` — căn tính/hệ sinh thái nghề nghiệp, không nằm trong trường class Slave.
- `Criminal` — lớp Slave riêng. Không dùng Undie nghề nghiệp làm bậc pháp lý/xã hội đối chiếu.

##### Color / visual-functional labels

- `Brown` — current confirmed use: màu jumpsuit đồng nhất của Civil; không phải rank Undie.
- `Black` — màu nhận dạng của Criminal; `Criminal` mới là class.
- `Red`, `Scarlet`, `Pink`, `Gray`, `Purple`, `Hazel`, `White` — mã kiến trúc Undie cũ đã nghỉ hưu; chỉ tái dùng qua quyết định canon riêng.

**Relations:** Citizen có thể đồng thời hành nghề Undie. Yellow là trạng thái kỷ luật độc lập; Undi là họ đồng phục nghề theo ngữ cảnh, không xác lập Yellow/Slave hoặc White→Citizen.

**UNKNOWN:** sự tồn tại của một penal class Brown ngoài nguồn hiện hành; ma trận quyền/mobility Criminal. Không tiếp tục hỏi full color/rank graph như thể nó còn là kiến trúc Undie hiện tại.

#### 3. JOB / LABOR REGIME

##### Civil

- Civil = labor buffer 5–10 năm.
- Không có billet thật thì không conversion.
- Billet phải có job, location, receiving unit, start time và deployment conditions.
- Applicant có thể từ chối trước conversion; sau conversion, accepted assignment là nghĩa vụ.
- Placement kết thúc → reserve/transitional duty → reassignment; unplaced Civil không phải unemployed Civil.
- Sau assignment, Civil hưởng labor law như Citizen trong phạm vi đã chốt.

##### Undie

- Hệ sinh thái nhiều nhánh nghề chồng lấn, không một job hoặc thang nghề chung.
- Citizen + người hành nghề Undie là tổ hợp đã chốt; gia nhập/rời nghề không đổi địa vị pháp lý.
- Môi trường hoạt động rộng và di động; sex work chỉ là một nhánh có thể có.
- Nghề, tính hợp pháp, dịch vụ, đồng thuận, hợp đồng và nơi làm việc là những biến riêng.
- Tương thích với nghĩa vụ Civil/Criminal hoặc điều kiện giấy phép cụ thể còn mở; `30` kiểm soát chi tiết.

---

##### Criminal

- Current confirmed regime: cực thấp/bẩn/nguy hiểm/không đáng dùng robot; ví dụ waste, hospital cleaning, sewer cleaning.
- `UNKNOWN / NEEDS USER RESOLUTION:` metallurgy/construction/factory list trong merged source có còn current hay không.

#### 3A. CIVIL AUDIT MATRIX

| Dimension | Latest confirmed canon | Status |
| --- | --- | --- |
| Entry | Apply → real billet → accept → final confirmation → conversion | CANON |
| Admission | Right to apply ≠ right to be admitted; no billet means no conversion | CANON |
| Legal status | Civil Slave; civic standing ngang Citizen nhưng legal status không đồng nhất | CANON |
| Labor allocation | Accepted assignment bắt buộc sau conversion | CANON |
| Right to quit | Có quyền từ chối billet trước conversion; unilateral exit khỏi Civil sau conversion chưa được định nghĩa | PARTIAL / UNKNOWN |
| Employer relation | Receiving unit nhận labor; labor law như Citizen; exact employer powers/liability chưa có | PARTIAL / UNKNOWN |
| State role | Receiving agency tạo demand; Civil authority kiểm tra/fill/allocate; hai authority không đồng nhất | CANON |
| Tax/fee | Former Civil có tax reduction/exemption tốt hơn Citizen thường; Civil có preferential Undie fee; exact rate/duration unknown | PARTIAL / UNKNOWN |
| Relocation cost | Chi phí cần thiết để placement xảy ra thuộc Civil system theo billet; exact reimbursement/housing unknown | PARTIAL / UNKNOWN |
| Public-service access | Quyền Citizen-equivalent “trong phạm vi đã chốt”; full service/access matrix chưa có | PARTIAL / UNKNOWN |
| Marriage | Current supplied sources chưa xác nhận Civil-specific marriage rule | UNKNOWN / NOT ESTABLISHED |
| Citizenship pathway | Review bắt đầu năm 5; tới năm 10 chưa được xét/duyệt thì lên Citizen trực tiếp | CANON |
| Resident pathway | Current supplied sources chưa xác nhận có hoặc không có resident-status pathway riêng | UNKNOWN / NOT ESTABLISHED |
| Exceptions | Exact year-5 criteria/authority/exceptions chưa chốt | UNKNOWN |
| Placement loss | Reserve/transitional duty rồi reassignment; không thành unemployed Civil | CANON |
| Mobility | Empire-wide billet pool; pre-conversion refusal; post-conversion location obligation; Civil→Citizen 5–10y; Undie affiliation không tạo Civil exit | CANON + bounded UNKNOWN |

#### 4. CAREER RANK

**Definition:** trục tiến trình nghề nghiệp dùng để mở facility/shopping/necessities và điều chỉnh Credits; không phải class hoặc color.

**Known values:** `Entry`, `Intermediate`, `Support`, `Advanced`, `Ultimate`.

**Relation:** Career Rank ngoài Undie là trục riêng. Đồ thị màu Undie cũ đã nghỉ hưu; không dùng Career Rank để khôi phục nó hoặc áp một tiến trình phổ quát cho nghề Undie.

**UNKNOWN / NOT ESTABLISHED:** full Career Rank rules và promotion formula ngoài phần đã chốt; chưa chốt việc dùng Career Rank trong nhánh nghề Undie mới.

#### 5. ZONE

**Definition:** operational geography, không phải status/class/rank.

**Known values:** Industrial, Commercial, Auctions, Entertainment. Capital có nhiều vòng; class/color có thể liên quan vùng hoạt động.

**Relations:** Undie có thể rời red-light district và đi trong đô thị; restriction nhắm vào disruptive activity hoặc specialized restricted points, không phải blanket presence ban. Capital có full/near-full Undie infrastructure; satellite cities có partial system.

**Phạm vi đô thị còn hiệu lực:** khu ăn chơi bao gồm phố đèn đỏ; tại thủ đô, cư dân phải từ 21 tuổi, kiểm soát bằng khuôn mặt/ID/vân tay. Đây là luật vào khu theo phạm vi cư dân đã chốt, không phải tuổi tuyển chung cho mọi nhánh Undie. Nội dung/quảng cáo người lớn bị hạn chế ngoài khu ăn chơi; hoạt động nghề trong đô thị không đồng nghĩa nội dung người lớn được phép khắp nơi.

**UNKNOWN:** full zone map, full access matrix, exact barrier/collar permission rules; staff/emergency exceptions chưa chốt. Không giữ quyền theo màu Undie cũ.

#### 6. CREDITS

**Definition:** Credits là tiền điện tử được nhà nước bảo chứng; cash là tiền cơ bản. Nhận Credits sau công việc là một giao diện đã mô tả, không phải định nghĩa mọi cách tạo/nhận Credits.

**Properties:** money; không phải Credit Score, Contribution Points, Career Rank, status hay class.

**Known uses của normal Credits:** ordinary consumption trong phạm vi được phép.

Facility proposals/upgrades và một số room/customization eligibility dùng source wording `credits` hoặc `credits nội bộ`; exact relation của chúng với normal personal Credits chưa chốt.

**UNKNOWN:** quan hệ kế toán chính xác giữa personal Credits và “credits nội bộ” của facility ngoài kiến trúc Undie đã nghỉ hưu; full credit economy. Không phục hồi uniform unlock/Pink cost/bonus dựa trên web cũ.

#### 7. CONTRIBUTION POINTS

**Definition:** vốn trách nhiệm/độ tin cậy theo vị trí.

**Properties:** không phải tiền, Credit Score hay morality score. Có thể reset khi tiến/lùi/đổi nghề trong các trường hợp đã chốt.

**UNKNOWN:** formula, authority và exact reset matrix ngoài phạm vi Undie. Contribution Points không còn là trục bắt buộc của hệ kinh tế/tiến trình Undie; việc còn mô tả nó ở miền khác không phục hồi kiến trúc ấy.

#### 8. OTHER ECONOMIC VARIABLES

##### Credit Score / Credit Line trong Undie

Kiến trúc Credit Score, Contribution Points theo nghề Undie và Credit Line thế chấp địa vị đã nghỉ hưu. Không còn điều kiện mobility/reset/White, khoản vay thế chấp người hay default→điều phối lao động ở cơ sở tư nhân.

Nợ tài chính, nghĩa vụ hợp đồng, ân tình xã hội và ân tình chính trị phải tách riêng; ân tình không phải tiền tệ. Nợ không tạo sở hữu người hoặc tự động cung cấp dịch vụ tình dục. Các nghiệp vụ vay/ứng trước/tài trợ mới còn cần thiết kế trong `30`.

---

##### Citizen credit profile / bad credit

- Financial/eligibility profile của Citizen; bad debt có thể làm giảm cơ hội việc làm.
- Không đồng nhất với tiền Credits hoặc các biến Undie đã nghỉ hưu; không tự xóa hồ sơ tín dụng Citizen vì retcon giới hạn ở Undie.

##### Legacy black credit

- Design history; không phải current canon.

#### 9. ACCESS PROFILE

**Definition:** quyền truy cập/di chuyển/dịch vụ được xác nhận qua collar/backend và rules; không phải class hay Career Rank.

**Known relations:**

- Career Rank có thể mở facility/shopping/necessities.
- Nghề/hoạt động, giấy phép, địa điểm và access là biến riêng; chưa chốt ma trận mới của Undie.
- Collar là administrative terminal cho ID, access, movement, task và enforcement links.
- Tư cách nghề nghiệp Undie không cho phép công quyền tùy tiện chặn subject; không gọi nó là legal status.
- Civil applicant chưa conversion không có Civil benefit.

**UNKNOWN:** full access matrix; permission changes của Career Rank ngoài phần đã chốt; public-service matrix Civil và điều kiện nghề/địa điểm Undie mới.

#### 10. BACKGROUND / PROVENANCE

**Definition:** nguồn gốc/hồ sơ lịch sử; không phải current operational classification.

**Known rules:**

- Sau voluntary Civil conversion, background vẫn ở hồ sơ nhưng không còn là biến vận hành chính.
- Không tạo Refugee/Nomad/Unemployed/Deserter Civil caste chỉ từ provenance.
- Lịch sử nghề nghiệp không phải địa vị pháp lý. Quy trình ẩn/truy xuất hồ sơ gắn với White→Citizen cũ không còn là mốc hiện hành; luật hồ sơ nghề mới chưa chốt.
- Genealogy của Yellow từ fake-Undie/impersonation không biến genealogy thành current class ontology.

**UNKNOWN:** exact provenance access law, truy xuất lịch sử nghề và treatment của non-voluntary Civil provenance ngoài phần đã chốt.

---

## Part II — Civil entry and allocation law

### AetherFire — Civil Entry / Allocation Law Canon

> **Trạng thái:** CANON — user-confirmed
>
> **Phạm vi:** luật chuyển `Citizen → Civil`, điều kiện tạo Civil billet, quyền từ chối trước conversion, nghĩa vụ allocation sau conversion, relocation, reassignment và giới hạn thẩm quyền của cơ quan Civil.
>
> **Không phải:** full labor code, full Civil bureaucracy, full benefit table, full review criteria năm 5, hoặc full manpower formula.
>
> **Nguyên tắc anti-drift:** Civil là **labor buffer 5–10 năm**, không phải welfare status và không phải bến chờ việc được nhà nước bảo lãnh.

---

### 1. Nguyên tắc trung tâm

```text
NO BILLET
→ NO CIVIL CONVERSION
```

Civil không vận hành theo mô hình:

```text
Citizen
→ thành Civil trước
→ rồi nhà nước mới tìm việc
```

Mà theo:

```text
Citizen
→ đăng ký Civil
→ tồn tại billet thật
→ applicant chấp nhận
→ final confirmation
→ Citizen → Civil
→ bắt đầu assignment
```

Do đó:

```text
CIVIL STATUS
= consequence of accepted real allocation

không phải

CIVIL STATUS
= quyền được nhà nước nuôi trong khi chờ allocation
```

---

### 2. Citizen có quyền đăng ký, không có quyền đòi được nhận

Citizen có quyền:

- tự nguyện đăng ký vào Civil;
- nhận thông tin về billet;
- từ chối billet trước khi status conversion có hiệu lực.

Nhưng:

```text
RIGHT TO APPLY
≠
RIGHT TO BE ADMITTED
```

Citizen không có quyền buộc nhà nước:

- tạo một billet mới theo sở thích cá nhân;
- giữ Civil slot khi chưa có việc thật;
- cấp Civil status trước rồi mới tìm placement.

---

### 3. Billet phải có trước status conversion

Một **Civil billet** tối thiểu phải xác định:

```text
công việc
+ địa điểm
+ đơn vị tiếp nhận
+ thời điểm bắt đầu
+ điều kiện ăn ở / di chuyển cần thiết
```

Billet không phải một lời hứa việc làm chung chung.

Nó là một allocation đủ cụ thể để nhà nước có thể thực thi ngay sau conversion.

---

### 4. Civil market là pool toàn AetherFire

Thiếu hoặc dư Civil không được đọc chỉ theo một thành phố.

```text
thủ đô dư nhu cầu Civil
≠
AetherFire dư nhu cầu Civil
```

Civil billet có thể tồn tại ở:

- thủ đô;
- thành phố vệ tinh;
- thuộc địa;
- các khu vực khác thuộc mạng Civil của AetherFire.

Người đăng ký Civil không có quyền mặc định yêu cầu:

> chỉ nhận Civil nếu được làm tại nơi đang cư trú.

Nếu billet hợp lệ nằm ở nơi khác, applicant có thể:

```text
chấp nhận
→ conversion

hoặc

từ chối
→ vẫn là Citizen
```

---

### 5. Voluntary entry đặt trước conversion

Cấu trúc đúng:

```text
VOLUNTARY ENTRY
≠
VOLUNTARY ALLOCATION AFTER ENTRY
```

Trước conversion:

- applicant được biết billet;
- applicant có quyền từ chối.

Sau khi:

```text
accepted billet
+ final confirmation
→ Citizen → Civil
```

thì assignment đã chấp nhận trở thành nghĩa vụ của Civil status.

Điều này không tự động có nghĩa Civil mất toàn bộ quyền cư trú trong mọi hoàn cảnh. Canon chỉ chốt rằng **địa điểm cần thiết để thực hiện billet đã chấp nhận đi cùng nghĩa vụ assignment**.

---

### 6. Đăng ký Civil không sinh Civil benefit

Trong giai đoạn:

```text
application
→ matching
→ billet offer
```

subject vẫn là Citizen.

Do đó:

- vẫn chịu market risk của Citizen;
- vẫn tự tìm việc nếu muốn;
- vẫn sống theo quyền và nghĩa vụ Citizen;
- không tự động phát sinh Civil allowance;
- không bắt đầu Civil 5–10 year clock.

Nếu AetherFire có trợ cấp Citizen khác, nó vận hành theo luật Citizen riêng, không phải vì subject đã nộp đơn Civil.

---

### 7. Mốc bắt đầu Civil lifecycle

Civil clock chỉ bắt đầu khi:

```text
billet hợp lệ
+ applicant chấp nhận
+ final confirmation
+ status conversion có hiệu lực
```

Không tính từ:

- ngày nộp đơn;
- ngày bắt đầu matching;
- ngày xếp hàng chờ Civil.

---

### 8. Relocation là phần của việc thực thi billet

Nếu billet yêu cầu chuyển tới:

- thành phố vệ tinh;
- thuộc địa;
- khu vực khác;

thì nhà nước phải có khả năng thực thi placement đó.

Chi phí cần thiết để relocation/placement xảy ra thuộc phía hệ thống Civil theo điều kiện billet.

Mục đích là tránh tình trạng:

```text
billet tồn tại trên giấy
nhưng applicant không thể thực sự tới nơi làm việc
```

---

### 9. Remote / strategic billet có thể dùng incentive

Billet ở nơi khó tuyển không bắt buộc phải dựa vào cưỡng ép trước conversion.

AetherFire có thể làm billet khó nhận hấp dẫn hơn bằng incentive như:

- housing tốt hơn;
- relocation được chi trả;
- phụ cấp;
- ưu tiên review từ năm 5;
- former-Civil tax benefit tốt hơn.

Các mức cụ thể chưa chốt.

Nguyên tắc:

```text
hard-to-fill billet
→ incentive cao hơn
```

Nếu applicant vẫn từ chối:

```text
→ họ vẫn là Citizen
```

---

### 10. Placement kết thúc không tạo Civil thất nghiệp

Nếu một billet chấm dứt trước khi Civil lifecycle kết thúc:

```text
Civil
→ placement ends
→ reassignment window
```

Subject vẫn là Civil.

Không được biến thành:

```text
Civil thất nghiệp
→ ngồi chờ trợ cấp
```

Trong reassignment window, subject thuộc **reserve / transitional duty**, có thể được dùng cho:

- training;
- maintenance;
- logistics support;
- temporary public works;
- công việc dự phòng phù hợp năng lực.

Do đó:

```text
UNPLACED CIVIL
≠
UNEMPLOYED CIVIL
```

---

### 11. Hai trạng thái vận hành, không phải hai legal status

Civil có thể tồn tại ở hai operational states:

```text
ACTIVE CIVIL
→ đang gắn với billet chính

RESERVE / TRANSITIONAL CIVIL
→ đang transit / training / reassignment
→ vẫn có nghĩa vụ lao động
```

Đây không phải hai class hay hai status pháp lý mới.

Chúng chỉ là hai trạng thái vận hành bên trong cùng Civil status.

---

### 12. Allocation authority không được tự tạo demand cho chính mình

Một điểm yếu trọng yếu cần khóa là tránh một cơ quan vừa:

```text
tự tuyên bố cần Civil
+ tự tạo billet
+ tự tuyển Citizen
+ tự phân bổ Civil
```

Cấu trúc canon chốt:

```text
cơ quan / ngành sử dụng lao động
→ yêu cầu billet / manpower need

Civil authority
→ kiểm tra / fill billet / allocation
```

Nguyên tắc:

```text
DEMAND AUTHORITY
≠
ALLOCATION AUTHORITY
```

Civil authority không tự phát minh nhu cầu lao động để mở rộng chính mình.

---

### 13. Manpower envelope

AetherFire có thể vận hành Civil dưới một giới hạn nhân lực được phê chuẩn ở cấp nhà nước:

```text
authorized manpower envelope
→ giới hạn số Civil mà hệ được phép giữ / fill
```

Exact formula, authority phê chuẩn và chu kỳ điều chỉnh chưa chốt.

Mục đích là ngăn:

```text
Civil demand tự phình
→ hút quá nhiều Citizen khỏi labor market
→ tạo dependency ngược vào Civil system
```

---

### 14. Core legal flow

```text
CITIZEN
   ↓
đăng ký Civil
   ↓
matching với billet thật
   ↓
nhận offer:
- job
- location
- receiving unit
- start time
- deployment conditions
   ↓
accept?
 ├─ NO  → vẫn là Citizen
 └─ YES
      ↓
final confirmation
      ↓
Citizen → Civil
      ↓
assignment có hiệu lực
      ↓
ACTIVE CIVIL
      ↓
placement kết thúc trước lifecycle?
 ├─ NO  → tiếp tục
 └─ YES
      ↓
RESERVE / TRANSITIONAL DUTY
      ↓
reassignment
      ↓
ACTIVE CIVIL
      ↓
5y review / 10y route
      ↓
Citizen
```

---

### 15. Các exploit mà cấu trúc này chặn

#### 15.1 Civil như bến đỗ an toàn không có việc

Sai pathway bị chặn:

```text
Citizen
→ xin Civil
→ thành Civil
→ chờ việc
→ sống bằng Civil support
```

Canon mới:

```text
NO BILLET
→ NO CIVIL CONVERSION
```

#### 15.2 Chỉ muốn Civil tại nơi mình thích

Applicant có quyền từ chối billet.

Nhưng:

```text
refuse billet
→ remain Citizen
```

Không có quyền:

```text
refuse billet
+ keep Civil status
```

#### 15.3 Địa phương dư nhưng satellite/colony thiếu

Civil allocation dùng pool toàn AetherFire.

```text
local surplus
≠ empire-wide surplus
```

#### 15.4 Placement mất thì Civil trở thành thất nghiệp

Sai.

```text
placement loss
→ reserve / transitional duty
→ reassignment
```

#### 15.5 Civil authority tự mở rộng vô hạn

Bị chặn bởi:

```text
DEMAND AUTHORITY
≠
ALLOCATION AUTHORITY
```

và có thể thêm manpower envelope ở cấp nhà nước.

---

### 16. Bản nén bắt buộc

```text
CIVIL = LABOR BUFFER 5–10 NĂM.

CITIZEN CÓ QUYỀN ĐĂNG KÝ, KHÔNG CÓ QUYỀN ĐÒI ĐƯỢC NHẬN.

NO BILLET → NO CIVIL CONVERSION.

BILLET PHẢI CÓ JOB + LOCATION + RECEIVING UNIT + START TIME + DEPLOYMENT CONDITIONS.

CIVIL MARKET LÀ POOL TOÀN AETHERFIRE, KHÔNG PHẢI CHỈ LOCAL MARKET.

APPLICANT CÓ THỂ TỪ CHỐI TRƯỚC CONVERSION.

TỪ CHỐI → VẪN LÀ CITIZEN.

SAU CONVERSION, ASSIGNMENT ĐÃ CHẤP NHẬN LÀ NGHĨA VỤ CIVIL.

APPLICATION KHÔNG SINH CIVIL BENEFIT VÀ KHÔNG CHẠY CLOCK 5–10 NĂM.

PLACEMENT ENDS → RESERVE / TRANSITIONAL DUTY → REASSIGNMENT.

UNPLACED CIVIL ≠ UNEMPLOYED CIVIL.

DEMAND AUTHORITY ≠ ALLOCATION AUTHORITY.

CIVIL AUTHORITY KHÔNG TỰ TẠO NHU CẦU CHO CHÍNH MÌNH.
```

---

### 17. UNKNOWN / chưa chốt

Không tự định nghĩa:

- exact Civil application form;
- exact billet approval procedure;
- exact authority tạo manpower envelope;
- exact manpower formula;
- exact remote-placement incentive;
- exact relocation reimbursement;
- exact housing standard;
- exact refusal cooling period;
- exact matching algorithm;
- exact reassignment duration;
- exact reserve-duty catalogue;
- exact limits của geographic reassignment sau khi đã vào Civil;
- exact year-5 review criteria;
- exact former-Civil tax benefit;
- full labor code áp cho Civil.

---

## Part III — Current cross-status and labor canon

> Imported once from the revamp anchor; Undie-specialized sections are located in the sibling Undie file.

### 0. Nguyên tắc đọc

Các distinction bắt buộc:

```text
SOCIAL HIERARCHY
≠ LEGAL STATUS
≠ CLASS
≠ OCCUPATION
≠ CAREER RANK
≠ AUTHORITY
≠ ASSET VALUE
```

Một actor có thể ở địa vị xã hội thấp nhưng có asset value rất cao, hoặc có backend quản trị như Slave nhưng frontend xã hội rất cao.

---

---

### 1. Thứ bậc xã hội chính thức

Thứ bậc các địa vị còn hiệu lực được ghi ở Part I §1A. Civil vẫn là Slave status có lifecycle riêng và civic standing ngang Citizen. Undie không còn là một caste/bậc cố định; quan hệ nghề không xác định địa vị xã hội.

---

### 2. Civil và hoạt động nghề Undie

Civil→Undie như chuyển địa vị một chiều đã nghỉ hưu. Gia nhập nghề không tự giải phóng Civil khỏi billet hoặc đổi địa vị; điều kiện làm nghề bên cạnh nghĩa vụ Civil còn mở.

---

### 5. Yellow

Citizen vi phạm lần đầu→Yellow một tuần→Citizen là chế tài tạm thời đã chốt. Yellow→Red/Undie, quota nghề ×2 và Undi làm dấu trừng phạt không còn là mốc mặc định. Trang phục Yellow và chế tài tái phạm cần quyết định riêng; không suy Yellow đã bị xóa.

---

### 6. POW

**CANON**

POW có hai lớp:

```text
FRONTEND / SOCIAL:
POW = Sĩ quan quân đội

BACKEND / ADMIN:
POW = Slave category
```

POW:

- làm việc theo điều phối;
- quản lý bằng collar như Slave thường;
- nhưng frontend ngang sĩ quan quân đội.

```text
backend Slave
≠ social inferiority
```

---

---

### 7. Civil Slave — Citizen-equivalent nhưng bị phân công

**CANON**

Civil Slave:

- có civic standing tương đương Citizen;
- không được nhục mạ vì status;
- quyền công dân tương đương Citizen trong phạm vi đã chốt;
- bị bắt buộc phân công công việc;
- sau khi được phân công, hưởng luật lao động như Citizen.

Nhục mạ Civil:

```text
→ phạt ×2
→ tính vào tội vu khống
+ sỉ nhục danh dự
```

trừ khi nội dung nói về hành vi phạm tội có thật.

---

---

### 8. Civil → Citizen

**CANON**

```text
Civil
→ 5 năm
→ bắt đầu được xét lên Citizen
```

Nếu đến 10 năm chưa được xét/duyệt:

```text
Civil
→ 10 năm
→ lên Citizen trực tiếp
```

Civil sau khi trở thành Citizen:

- được miễn thuế hoặc giảm thuế tốt hơn Citizen thường;
- ưu đãi này gây ghen tị mạnh từ Trung lưu trở xuống.

---

---

### 14. Người hành nghề Undie vi phạm pháp luật

Undie không phải class hoặc địa vị pháp lý. Không tự duy trì hệ tư pháp/kỷ luật riêng thay luật thường chỉ vì nghề. Hành vi, địa vị thực, luật nghề/hợp đồng và cơ quan có thẩm quyền phải được xác định trong đúng phạm vi; ma trận chế tài còn mở.

---

### 15. Criminal

**CANON**

Criminal là Slave class.

Nguồn vào:

```text
đối diện án tử
→ thỏa thuận nhận tội
→ tránh tử hình
→ Criminal Slave
```

Criminal làm các việc cực thấp mà robot còn “chê”, ví dụ:

- rác thải sinh hoạt;
- vệ sinh bệnh viện;
- vệ sinh cống rãnh;
- các việc tương tự bẩn/nguy hiểm/không đáng dùng robot.

Criminal vẫn có quyền cơ bản. So sánh điều kiện sống với một lớp Undie thấp hơn Civil đã bị supersede; không tự tạo chuẩn sống mới cho người hành nghề.

Không tha bổng.

Không tự suy `không tha bổng = không kháng cáo / không tái thẩm`.

---

---

### 28. Bailout — correction

**CANON / SUPERSEDE**

Ngoại lệ loại trừ Undie theo class cũ đã bị supersede. Quy tắc Citizen bên dưới giữ nguyên; không tự chốt ma trận áp dụng mới theo nghề hoặc mọi nhánh dịch vụ.

Nó áp dụng cho **Citizen từ Thượng lưu trở xuống**.

```text
Citizen từ Thượng lưu trở xuống
→ bailout rất nặng
→ tối đa 2 lần
→ sau đó phải ra tòa
```

Tại tòa:

```text
có tiền
→ xử như dân sự

không có tiền
→ nguy cơ xuống Criminal rất cao
```

Core design:

```text
cho phép hành vi rủi ro
→ Citizen tự chịu trách nhiệm
→ vi phạm tạo legal trigger
→ fine / bailout / civil liability
→ extraction
```

Không dùng tư cách nghề Undie để thay quy tắc theo địa vị pháp lý; xem mục 14 về phần triển khai chưa chốt.

---

---

### 29. Bia rượu

**CANON**

Không giới hạn độ tuổi uống bia rượu.

Triết lý:

```text
Citizen
→ tự ý thức
→ tự chịu trách nhiệm hành vi
```

AetherFire cố ý không chặn quá nhiều ở đầu vào, nhưng phạt nặng ở downstream behavior.

Ví dụ:

- sàm sỡ cư dân Hoa Nguyệt;
- vận động tay chân/bạo lực với Undie.

---

---

### 32. Citizen career system

**CANON**

Citizen có:

- nghề riêng;
- promotion riêng;
- career progression riêng.

Citizen có thể đồng thời là người hành nghề Undie. White→Citizen đã nghỉ hưu; không có career class mới được tạo từ việc rời nghề.

---

---

### 33. Civil → Citizen có tax privilege

**CANON**

Former Civil sau khi thành Citizen:

```text
→ miễn thuế hoặc giảm thuế tốt hơn Citizen thường
```

Điều này gây ghen tị mạnh từ Trung lưu trở xuống.

---

---

### 34. Citizen → Civil → Citizen để hưởng policy

**CANON**

Citizen có thể tự xuống Civil rồi quay lại Citizen và hưởng policy giảm/miễn thuế như former Civil khác.

Nhưng:

```text
Civil → Citizen
→ review từ 5 năm
→ có thể kéo tới 10 năm
```

nên gần như không ai cố tình dùng route này chỉ để tax arbitrage.

---

---

### 35. Citizen và Undie

Citizen có thể gia nhập nghề Undie mà không mất citizenship/legal status. Quyền rời nghề và hậu quả hợp đồng/tài chính truy nguyên được do `30` kiểm soát; không còn one-way status entry hoặc White exit.

---

### 36. Citizen có thể thất bại kinh tế

**CANON**

Citizen status không bảo đảm:

- có việc;
- không nợ;
- không bị xiết nợ;
- không bị nợ gia đình;
- không có bad credit;
- không bị giảm khả năng tìm việc do credit status/vay xấu.

Có thể hình thành vòng:

```text
thất nghiệp / nợ
→ credit profile xấu
→ cơ hội việc làm giảm
→ thu nhập giảm
→ credit profile tiếp tục xấu
```

---

---

### 37. Civil là fallback ổn định; Undie là fallback khác

**CANON**

Citizen có thể:

```text
nuốt sĩ diện
→ xuống Civil
```

đổi lại:

- có job;
- có payment;
- có chế độ;
- có labor protection;
- có route 5–10 năm quay lại Citizen.

Civil:

```text
employment stability ↑
occupational agency ↓
prestige ↓
```

Undie có thể là lựa chọn nghề nghiệp, không phải fallback đổi địa vị tương đương Civil. Gia nhập không tự giải quyết nợ, thất nghiệp hoặc nghĩa vụ Civil.

---

---

### 41. Civil được ưu đãi phí khi dùng Undie

**CANON**

Civil có thể sử dụng dịch vụ Undie.

```text
Civil
→ preferential fee
```

Ưu đãi này là thêm một nguồn ghen tị từ Citizen, nhất là Trung lưu trở xuống.

Cumulative grievance:

```text
Civil
→ job bảo đảm
→ labor law như Citizen
→ phí Undie ưu đãi
→ route trở lại Citizen
→ tax benefit hậu Civil
```

trong khi Citizen thường phải chịu market risk.

---

---

### 42. Không có homeless population ổn định

**CANON**

AetherFire không duy trì người vô gia cư như một social status lâu dài.

Nếu một người rơi vào vô gia cư:

```text
homeless
├─ → Civil Slave
└─ → trục xuất
```

Không có route thứ ba đã được chốt.

---

---

### 42A. Disability và debt

**CANON**

Disability làm mất khả năng hoạt động được xử lý bằng magic + technology hybrid.

```text
disability
→ hybrid treatment
→ phục hồi khả năng hoạt động
→ phát sinh debt
```

Do đó:

```text
social problem visibility ↓
individual economic obligation ↑
```

AetherFire có thể tuyên truyền rằng:

- không có người vô gia cư;
- không ai bị bỏ mặc vì khuyết tật;

trong khi cost được chuyển thành debt/status/economic obligation.

---

---

### 43. Core exploitation design — phạm vi còn hiệu lực

AetherFire có thể giữ tự do/lựa chọn rủi ro→trách nhiệm cá nhân→legal/economic trigger→fine/bailout/debt/status extraction. Ví dụ tuổi uống rượu và Citizen→Civil có xác nhận vẫn còn trong phạm vi đã chốt.

Không dùng Undi để tạo nhầm lẫn/hạ nhục rồi phạt như mục đích mặc định, hoặc dùng nghề Undie làm một engine kiểm soát Slave. Nợ, thị trường, patronage và lạm dụng có thể tạo hậu quả khi có cơ chế riêng; retcon không khẳng định mọi bóc lột đã biến mất.

---

### 44. Địa vị và nghề là hai quan hệ khác nhau

```text
Citizen → accepted billet + final confirmation → Civil
Civil → review từ năm 5 / tới năm 10 chưa duyệt → Citizen
Citizen → first offense → Yellow một tuần → Citizen
death-sentence exposure → plea → Criminal
```

Citizen từ Thượng lưu trở xuống vẫn có bailout tối đa hai lần→tòa→nguy cơ Criminal khi không có tiền, trong phạm vi đã chốt.

```text
Citizen + nghề Undie
gia nhập/rời nghề Undie ≠ legal-status transition
```

Chế tài tái phạm Yellow và điều kiện nghề cho Civil/Criminal còn mở; không nối lại đồ thị cũ.

---

### 46. UNKNOWN bắt buộc giữ

- Full hierarchy/progression của nghề Citizen; promotion formula.
- Review Civil năm 5, authority, ngoại lệ, tax rates/duration.
- Criminal rights/labor matrix, bailout amount và court procedure.
- Yellow repeat timing, chế tài mới và trang phục.
- Nghề/giấy phép/hợp đồng/access Undie mới, tương thích nghĩa vụ Civil và eligibility Criminal.
- Luật hồ sơ, kế vị/tước vị riêng không suy từ nghề.
- Medical debt terms; disability không chữa được bằng hybrid treatment; vô gia cư không thể trục xuất.
- Public-content moderation, staff/emergency exceptions của khu ăn chơi và các triển khai dịch vụ ngoài phần đã chốt.
- Các nhóm unknown Undie mới nằm ở `30` §17 và `92`; không giữ threshold/rank/status collateral cũ như kiến trúc hiện hành.

---

### 47. Tóm tắt ranh giới hiện hành

Citizen = Civil về civic standing, không đồng nhất legal status. Civil bị phân công nhưng hưởng luật lao động như Citizen trong phạm vi đã chốt; lifecycle 5–10 năm và tax advantage giữ nguyên. POW frontend ngang sĩ quan, backend thuộc Slave security category. Criminal giữ pipeline riêng và quyền cơ bản trong phần đã chốt.

Undie = nghề/hệ sinh thái, không phải Slave/caste/punishment. Citizen + Undie có thể đồng thời; entry/exit không đổi địa vị. Không còn đồ thị màu, White→Citizen, Yellow→Red/Undie, triệt sản bắt buộc hoặc web tín dụng thế chấp người.

Cash + Credits được nhà nước bảo chứng; nợ ≠ sở hữu người ≠ tự động dịch vụ tình dục. Hồ sơ tín dụng Citizen và luật Civil ngoài phạm vi không bị xóa.

Undi là họ đồng phục nghề theo ngữ cảnh; Hoa Nguyệt appropriation có ý định thật nhưng không được người ngoài chứng minh chắc chắn. Tử vong, nghề, an ninh và MC2 theo mốc `30` mới; chưa tự viết các triển khai còn mở.

Ưu đãi phí dịch vụ cho Civil, luật tuổi uống rượu, homelessness và hybrid disability treatment/debt giữ đúng phạm vi cũ; không mở rộng chúng thành luật của mọi nhánh Undie.

---

## Part IV — Civil strategic rationale and provenance boundary

### 1. Civil Slave — chức năng chiến lược

**CANON**

Civil Slave tồn tại chủ yếu để xử lý **độ biến động của thị trường lao động tự do**.

AetherFire là một đế quốc đi chiếm và khai thác tài nguyên bên ngoài. Với cấu trúc hậu cần dày đặc, biến động nhân lực tại các mắt xích có thể trở thành thảm họa cấp quốc gia.

Quan hệ cốt lõi:

```text
thị trường lao động tự do
→ biến động nhân lực
→ rủi ro đứt công suất hậu cần

Civil Slave
→ pool lao động ổn định
→ giảm biến động
→ tăng khả năng dự báo và duy trì công suất dài hạn
```

Không đọc Civil Slave đơn giản như:

```text
welfare cho người nghèo
```

hoặc:

```text
lao động rẻ
```

Các bảo đảm vật chất và khả năng hấp thụ dân cư bất ổn là một phần của trade-off, nhưng lý do chiến lược trung tâm là **ổn định nhân lực và hậu cần**.

---

---

### 2. Voluntary Civil Slave — background bị vô hiệu hóa về mặt vận hành

**CANON**

Đối với route tự nguyện:

```text
background khác nhau
→ intake
→ xác nhận cuối
→ vượt status boundary
→ Civil Slave
```

Sau khi vượt ranh giới chuyển status:

- background cũ vẫn tồn tại trong hồ sơ;
- background không còn là biến vận hành chính;
- subject được quản trị theo status/class/job hiện tại.

Không tự tạo các caste như:

```text
Refugee Civil Slave
Nomad Civil Slave
Unemployed Civil Slave
Deserter Civil Slave
```

chỉ từ nguồn gốc trước intake.

Điểm chống drift:

```text
background
= provenance / archival record

current status
= operational classification
```

Mệnh đề này áp cho **voluntary status conversion**; không tự lan sang POW, Criminal, Yellow hoặc các route đặc biệt.

---
