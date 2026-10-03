# Quy trình cho gói AetherFire Project

Dùng reference này khi cần chọn mốc package, sửa hoặc chứng nhận gói, hoặc khi metadata package ảnh hưởng trực tiếp tới kết luận. Với LOOKUP hẹp, chỉ đọc metadata tối thiểu để tìm đúng nguồn hiện hành.

Nhận diện package qua `00_AETHERFIRE_CONSOLIDATION_INDEX.md`, `MANIFEST.md`, `build_consolidation.py` và `Source_Archive/`. Xác minh vai trò bằng nội dung hiện hành thay vì suy từ tên file.

## 1. Preflight và vai trò

1. Đọc index để biết reading order, domain boundaries và source bị loại trừ.
2. Đọc manifest để phân biệt current sources, các vùng generated và archived snapshot; ghi hash/status ban đầu trong phạm vi thay đổi.
3. Đọc phần liên quan của reconciliation record để biết quyết định, unresolved item và provenance đang có hiệu lực.
4. Đọc đầy đủ nguồn canon thuộc phạm vi audit. Chỉ đọc logic Python khi cần truy hoặc sửa phép kiểm tra/cập nhật; logic builder không phải bằng chứng canon.

Các file root hiện hành là nguồn được duy trì trực tiếp. `Source_Archive/` là lịch sử/provenance, không phải đầu vào hoặc nguồn dự phòng để tái dựng canon. Archive presence không chứng minh canon acceptance. `build_consolidation.py` chỉ kiểm header, catalog, cross-domain references và current hashes; `--write` chỉ sửa vùng generated catalog trong index cùng vùng generated metadata/hash trong manifest.

## 2. Lập kế hoạch thay đổi

Trước thay đổi nhiều domain, build pipeline hoặc retcon có hệ quả chéo, trình bày quyết định đã chốt, phạm vi file/vùng được sửa, invariants và unresolved items phải giữ, cùng kiểm tra package và ngữ nghĩa sẽ chạy. Kế hoạch không mở rộng quyền sửa ngoài quyết định đã chốt.

## 3. Cập nhật package sau phê duyệt

1. Ghi hash/status và danh sách file được phép tác động.
2. Giữ archived source cũ nguyên vẹn; nguồn mới cần lưu archive phải được lưu byte-exact với tên không trùng. Việc lưu archive không tự nhập nội dung vào canon.
3. Sửa current sources và reconciliation trong đúng phạm vi đã duyệt. Không sửa tay các vùng generated; không dựng lại current sources từ archive.
4. Chạy `python -B '<project-root>/build_consolidation.py' --write` khi cần đồng bộ catalog/metadata/hash, rồi chạy `--check`.
5. Đọc lại file đầu ra thực tế có liên quan. Đối chiếu quyết định, mốc cũ và nguồn còn hiệu lực; kiểm cả nội dung được đổi lẫn nội dung phải giữ.
6. Không chuyển mốc khi có thay đổi ngoài phạm vi, nội dung được duyệt bị thiếu, unresolved item bị xóa hoặc kiểm tra package thất bại.

## 4. Cổng xác minh trước khi báo hoàn tất

Chạy kiểm tra chỉ đọc:

```powershell
python -B '<AetherFire Project path>\build_consolidation.py' --check
```

Hoặc dùng wrapper của skill; wrapper gọi cùng lệnh và báo lỗi nếu Python trả exit code khác 0:

```powershell
& '<skill-root>\scripts\verify_aetherfire_package.ps1' -ProjectRoot '<AetherFire Project path>'
```

Có thể truyền `-PythonExecutable '<python executable path>'` nếu cần chọn interpreter cụ thể.

`PASS` xác nhận các kiểm tra cấu trúc/catalog/current hashes do validator hiện hành thực hiện. Kiểm tra này không đọc/re-hash archive, không rebuild toàn bộ canon và không chứng minh canon đúng hoặc LLM tuân thủ. Sau đó vẫn phải đối chiếu ngữ nghĩa với quyết định, kiểm nguồn ngoài phạm vi không đổi và báo mọi UNKNOWN/DEFERRED còn lại. Nếu thay validator, chạy thêm test liên quan trong package.
