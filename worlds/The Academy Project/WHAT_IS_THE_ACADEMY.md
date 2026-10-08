# The Academy — What It Is, How It Works, and Why It Exists

**Trạng thái:** Orientation / author-confirmed purpose
**Phạm vi:** mô tả cấp cao để người đọc mới hiểu đúng The Academy trước khi đi vào source chi tiết.
**Không phải:** world bible hoàn chỉnh, engine specification, source thay thế cho V1.5/V2, hoặc permission để lấp các vùng UNKNOWN.

Đọc tài liệu này cùng README.md, Narrative Engine — Core Design Philosophy, V1.5 Architecture Baseline, Historical Influence Potential, genealogy và source engine-specific khi cần.

---

# 1. The Academy là gì?

Cách mô tả ngắn nhất:

> **The Academy là một fanfiction/daydream simulation engine.**

Nó không được tạo ra chủ yếu để sinh prose, chapter, screenplay hay một văn bản fanfiction hoàn chỉnh.

Use case gốc là:

    user đang đọc / xem / chơi một Host Fiction
            ↓
    chọn một actor / HIP / target đáng quan tâm
            ↓
    The Academy tạo thêm setting, trải nghiệm,
    quan hệ, pressure hoặc Narrative Engine
            ↓
    actor trở lại / tiếp tục trong Host Fiction
    với state đã thay đổi
            ↓
    user tiếp tục mô phỏng trong đầu:
    "với state mới này, cảnh / arc / lịch sử sẽ đổi thế nào?"

Host Fiction là fiction nền mà user đang dùng để simulation. Nó có thể là một tác phẩm có sẵn, fan-created setting hoặc fiction gốc. The Academy không sở hữu Host Fiction và không mặc định thay ontology của Host Fiction.

    ENGINE APPLIES TO HOST
    != ENGINE CONTAINS HOST

    HOST FICTION
    != SUBSYSTEM OF THE ACADEMY

The Academy cung cấp thêm causal structure cho simulation. Host Fiction vẫn cung cấp local reality: nhân vật, lịch sử, social structure, metaphysics, magic, technology và các luật khác của chính nó.

---

# 2. Output chính không phải text

Output quan trọng nhất của The Academy là một trạng thái simulation mới, không phải một đoạn văn.

Ví dụ dùng actor baseline A:

    A0
    → trải qua The Academy
    → tích lũy experience X
    → knowledge Y
    → capability / power Z
    → peer-HIP exposure và các modifier khác abc
    → trở về Host Fiction
    → A1

Có thể dùng phép ghi nhớ A1 ≈ AXYZabc. Đây chỉ là shorthand cho state transformation, không phải hash theo nghĩa kỹ thuật.

A1 vẫn có continuity với A0, nhưng không còn cùng causal state.

    A0 + canon event E
    → canon trajectory O

    A1 + cùng event E
    → trajectory có thể khác

The Academy không cần tự viết toàn bộ trajectory mới thành prose. User có thể tiếp tục đọc/xem Host Fiction và mentally recompute những cảnh bị state mới tác động.

---

# 3. V1.5 làm gì?

V1.5 là institutional Academy runtime trước tốt nghiệp.

Nó dùng một setting Academy xuyên reality/time làm môi trường causal:

    Host Fiction / actor baseline
            ↓
    HIP selection / recruitment / consent
            ↓
    THE ACADEMY V1.5
            ↓
    institutional Narrative Engines
    + education
    + cross-civilization exposure
    + peer-HIP interaction
    + choices / agency
            ↓
    graduation
            ↓
    RETURN TO ORIGIN
            ↓
    modified actor state

Boundary quan trọng:

    RETURN TO ORIGIN
    = V1.5 TERMINUS

V1.5 không chỉ buff actor. Actor có thể trở về với thay đổi về kinh nghiệm, tri thức, kỹ năng hoặc capability, worldview, quan hệ, exposure với civilization khác, ký ức và kinh nghiệm với HIP khác, cùng các modifier khác do institutional engines và lựa chọn của chính actor tạo ra.

Cross-HIP interaction là một phần causal quan trọng. HIP không chỉ học từ staff hoặc institution mà còn thay đổi vì tiếp xúc với các HIP đến từ những reality khác.

V1.5 thay đổi conditions, option space và actor state. Nó không preselect một historical outcome.

---

# 4. V2 làm gì?

V2 là operational profile tập trung vào post-grad Narrative Engine causality.

Sau khi actor đã có baseline bị biến đổi — từ V1.5 hoặc từ một configuration khác — Narrative Engines có thể tiếp tục hoạt động trong hoặc qua Host Fiction.

Cách hiểu cấp cao:

    Host Fiction timeline ─────────────────────────→
                   actor / HIP
                        │
                        ├── canon events
                        ├── existing relations
                        └── Narrative Engine pressure / intervention
                                  ↓
                         trajectory influence tăng
                                  ↓
                         divergence space lớn hơn

Nếu V1.5 chủ yếu tạo một modified baseline, V2 chủ yếu làm tăng hoặc biến đổi khả năng causal influence của actor hoặc target khi Host Fiction tiếp tục chạy.

Shorthand:

    V1.5
    ≈ character-state transformation through an Academy setting

    V2
    ≈ trajectory-influence amplification through Narrative Engines

Đây là mô tả chức năng cấp cao, không phải universal schema cho mọi Narrative Engine. Mỗi engine có architecture riêng. Không được suy rằng mọi engine có cùng trigger, Governor, Catalyst, authority, interface hoặc termination condition.

---

# 5. V1.5 và V2 không phải software version ladder

Tên version ghi genealogy và operational profile, không có nghĩa V2 mới hơn thì V1.5 bị deprecated.

    V1.5 remains valid.
    V2 remains valid.

    GENEALOGY != CURRENT HIERARCHY
    LATER EXTERNALIZATION != ONTOLOGICAL REPLACEMENT

Một fiction/daydream configuration có thể dùng V1.5, V2 hoặc một cách ghép được author xác nhận. Điều kiện chính xác cho từng configuration phải theo source hiện hành; không tự invent.

---

# 6. HIP đóng vai trò gì?

HIP = Historical Influence Potential.

HIP là một evaluation gateway, không phải universal score. Nó không tự định nghĩa power level, protagonist importance, morality, chosen-one status hay một thang điểm lịch sử cố định. Criteria đến từ context.

Trong The Academy, HIP hữu ích vì hệ quan tâm đến actor có khả năng trở thành causal variable đáng mô phỏng. Actor không cần phải mạnh nhất; một actor có vị trí causal phù hợp có thể tạo divergence rất lớn sau một thay đổi tương đối nhỏ.

---

# 7. Vì sao The Academy tồn tại?

Câu hỏi gốc của Academy-style simulation là:

> **Nếu những cá nhân có khả năng ảnh hưởng lịch sử được tiếp xúc với những nền văn minh, tri thức, con người và cơ chế mà Host Fiction gốc không cung cấp, rồi trở về đúng thế giới của mình, chuyện gì sẽ xảy ra?**

The Academy tồn tại để tạo điều kiện cho loại simulation đó.

    baseline actor
    + foreign exposure
    + institutional pressure
    + peer-HIP interaction
    + actor agency
    → modified actor state
    → return to Host Fiction
    → historical / narrative divergence

Về sau, Narrative Engine architecture mở rộng khả năng này:

    modified baseline
    + post-grad Narrative Engine causality
    → stronger / different influence on trajectory

Mục tiêu không phải chọn kết thúc tốt nhất, cũng không phải ép canon thành một outcome do engine quyết định.

    ENGINE CHANGES CONDITIONS / PRESSURE / TRAJECTORY
    != ENGINE WRITES THE OUTCOME

---

# 8. The Academy được dùng như thế nào trong thực tế?

The Academy chủ yếu phục vụ daydreaming / internal simulation while consuming fiction.

Một session có thể trông như:

1. User đọc / xem Host Fiction.
2. User chọn actor hoặc target.
3. User áp V1.5, V2 hoặc engine phù hợp.
4. Actor nhận state / pressure / relation mới.
5. User tiếp tục theo mạch Host Fiction.
6. Khi canon event xảy ra, user mentally evaluates: actor ở state hiện tại sẽ phản ứng thế nào?
7. Consequence mới tạo branch simulation.
8. User tiếp tục mô phỏng branch đó.

Host Fiction tự cung cấp rất nhiều rendering: hình ảnh, dialogue, setting, actor, timeline, canon event và emotional context.

The Academy không cần tái sản xuất toàn bộ chúng thành text. Nó can thiệp vào state và causality, rồi user chạy phần còn lại trong đầu.

---

# 9. Vì sao project khó externalize?

The Academy tồn tại như một paracosm nội tại lâu hơn rất nhiều so với repository và vocabulary hiện tại.

Nhiều mechanism tồn tại trước khi có tên formal. Ngược lại, một số composition hiện tại mới hơn material cấu thành nó.

Vì vậy phải giữ riêng:

- genealogy;
- current ontology;
- operational profile;
- source authority;
- epistemic state.

Không được suy:

    old material
    → old current architecture

    new vocabulary
    → new underlying mechanism

    same name
    → same role in every profile

Repository chỉ là externalized control surface.

    INTERNAL PARACOSM STATE
    != EXTERNALIZED REPOSITORY STATE
    != CURRENTLY LOADED LLM CONTEXT

Thiếu source không cho phép tự hoàn thiện graph.

---

# 10. Thuật ngữ trong project không mặc định mang nghĩa software

Các từ engine, module, interface, architecture và pipeline là vocabulary nội bộ được dùng để externalize một hệ worldbuilding/daydream simulation.

Không được tự động import nghĩa từ software engineering nếu source của The Academy định nghĩa khác.

    Narrative Engine != software runtime
    Module != software package
    Interface != automatically an API
    Architecture != automatically a parent-child hierarchy

Local glossary và source của The Academy có precedence đối với nghĩa nội bộ.

---

# 11. Anti-drift tối thiểu

    THE ACADEMY IS PRIMARILY A FANFICTION / DAYDREAM SIMULATION ENGINE.

    TEXT GENERATION IS NOT ITS PRIMARY OUTPUT.

    HOST FICTION IS THE FICTION BEING SIMULATED,
    NOT A SUBSYSTEM OWNED BY THE ACADEMY.

    V1.5 TRANSFORMS ACTOR STATE THROUGH AN INSTITUTIONAL ACADEMY SETTING.

    V2 ADDS POST-GRAD NARRATIVE-ENGINE CAUSAL PRESSURE
    AND CAN AMPLIFY OR ALTER TRAJECTORY INFLUENCE.

    RETURN TO ORIGIN IS THE V1.5 TERMINUS.

    THE SAME CHARACTER MAY RETURN WITH A DIFFERENT CAUSAL STATE.

    HIP IS A CONTEXT-SUPPLIED EVALUATION GATEWAY,
    NOT A UNIVERSAL POWER OR IMPORTANCE SCORE.

    ENGINE CHANGES CONDITIONS / PRESSURE / TRAJECTORY.
    ENGINE DOES NOT AUTOMATICALLY WRITE OUTCOME.

    V1.5 != DEPRECATED BY V2.
    GENEALOGY != CURRENT HIERARCHY.
    INTERACTION != CONTAINMENT.
    CO-OCCURRENCE != DEPENDENCY.
    UNKNOWN != PERMISSION TO INVENT.

---

# 12. One-paragraph description

**The Academy là một fanfiction/daydream simulation engine dùng để thay đổi causal state của actor trong một Host Fiction rồi quan sát trajectory mới trong đầu user. V1.5 cung cấp một multiversal Academy setting nơi HIP đi qua institutional Narrative Engines, học hỏi, tương tác với HIP khác và tích lũy các modifier trước khi trở về world gốc; V2 tiếp tục đưa Narrative Engine causality chạy cùng Host Fiction để tăng hoặc biến đổi khả năng actor ảnh hưởng lên trajectory. The Academy không được thiết kế chủ yếu để sinh fiction text: user có thể đọc/xem chính Host Fiction làm renderer, mentally patch actor state và tiếp tục simulation từ các canon event. Hệ giữ agency và không preselect outcome; engine thay đổi điều kiện và causal pressure, còn trajectory cụ thể phát sinh từ actor, host rules, interaction và lựa chọn trong simulation.**
