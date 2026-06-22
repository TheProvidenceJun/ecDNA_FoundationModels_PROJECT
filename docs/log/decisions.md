# decisions.md — 무엇을·왜·대안은 (append-only, cowork만 쓰기)

> 되돌리기 어렵거나 방향을 바꾸는 결정을 기록. 형식 아래 참고.

---

## 2026-06-03 — docs/ 골격을 cold start에서 즉시 생성
- **무엇**: CLAUDE.md §3 구조대로 docs/ 골격을 생성하되, constitution·plan은 PLACEHOLDER 스텁으로만 두고 실내용은 미합의 상태로 남김.
- **왜**: 메모리 인프라(state/log)가 없으면 다음 세션이 인계받을 수 없음. 골격은 즉시 필요하나, 실내용은 사람 합의가 필요하므로 분리.
- **대안**: (a) 전부 한 번에 채움 — 거부(미합의 추측 위험). (b) 골격도 안 만들고 합의부터 — 거부(메모리 부재 지속).

## 2026-06-03 — spec/report 템플릿 확정, AGENTS.md는 다음 세션으로 미룸
- **무엇**: `tasks/specs/_TEMPLATE.md` · `tasks/reports/_TEMPLATE.md` 를 현재 구조로 확정(사람 합의). codex 부팅 진입점 AGENTS.md는 오늘 만들지 않고 다음 세션으로 미룸.
- **왜**: spec↔report 계약 골격을 먼저 단단히 하고, AGENTS.md는 constitution 실내용과 함께 묶어 다음 세션에 일관되게 작성하는 편이 낫다는 사람 판단.
- **함의**: 다음 세션 전까지 codex에게 정식 발주 불가(진입점 부재). 그 전까지는 spec 초안만 준비 가능.

## 2026-06-03 — git 커밋 행위는 사람 전용
- **무엇**: `git commit`/`push` 등 커밋 행위는 사람만 한다. cowork는 파일을 디스크에 쓰는 데까지만 하고, 커밋이 필요하면 커밋 메시지를 제안한 뒤 **멈춘다**.
- **왜**: 저장소 이력(되돌리기 어려운 영속 변경)에 대한 최종 통제권을 사람이 갖기 위함. §5 제약 규약("위험 작업은 사람 승인")의 구체화.
- **반영**: CLAUDE.md §4에 한 줄 추가. constraints.md의 강제 메커니즘 표에도 추후 반영 필요(현재는 soft 규칙).
- **대안**: cowork가 커밋까지 자동화 — 거부(이력 통제권 상실 위험).

## 2026-06-21 — AGENTS.md 확정 (codex를 "좁게 가두는" 진입점)
- **무엇**: 저장소 루트에 AGENTS.md 작성·확정. codex는 매 작업 시 (constraints.md, conventions.md, 지정 spec 하나)만 읽고, 코드/reports/sessions.md에만 쓰며, 막히면 멈춘다.
- **왜**: codex에 전모를 주면 spec 범위를 넘어 "도움이 되려" 딴짓을 한다. 시야를 좁히는 것이 관찰가능성·소유권을 지킨다. 정합성 (A)(B)로 reports 템플릿·specs §7과 모순 없음 확인.
- **대안**: codex에 STATE·plan·roadmap을 다 읽힘 — 거부(범위 이탈 유발).

## 2026-06-21 — AGENTS.md 자동 로드 가정은 '미검증 전제'로 표시만
- **무엇**: "codex-GUI가 매 작업 시작 시 AGENTS.md를 자동 로드한다"는 가정을 AGENTS.md 안에 PREMISE(unverified)로 명시. 실제 검증(코드 발주로 확인 등)은 이번 세션에 하지 않음.
- **왜**: 아직 codex-GUI 동작을 사람이 확인하지 못함. 문서 표시로 위험을 가시화하는 것으로 이번엔 충분하다는 사람 판단. 자동 로드 안 되면 사람이 발주 시 직접 제시하면 됨.
- **후속**: 사람이 codex-GUI에서 자동 로드 여부 확인 후 이 결정 로그에 결과 append.

## 2026-06-21 — Phase A.3(dataset 매핑)은 codex spec이 아니라 사람(+도구1) 작업
- **무엇**: 가이드 Phase A의 핵심 deliverable인 A.3(dataset 매핑·target list 확정)을 codex 자동화 발주 대상에서 제외하고, 사람(+도구1)이 직접 수행하는 작업으로 둔다. roadmap.md·current_phase.md 양쪽에 일관 반영.
- **왜**: (1) AmpliconRepository.org academic email 등록·계정 인증은 본질적으로 사람 몫. (2) 어느 cell line을 우선할지는 판단이 섞인 큐레이션이라 spec으로 좁히기 어렵고, 잘못 자동화하면 범위 이탈·오큐레이션 위험.
- **대안**: A.3을 codex spec으로 발주 — 거부(계정 인증 불가 + 판단 자동화 부적합). 부분만 발주(예: CCLE 다운로드 스크립트) — 향후 필요 시 별도 검토 여지는 남김.

## 2026-06-21 — Phase 0 완료조건에 harness smoke test 추가
- **무엇**: Phase 0 졸업 조건에 "시험용 spec 1건을 codex에 발주 → AGENTS.md 부팅·쓰기경계·report 의무 준수를 report·sessions.md 흔적으로 확인"을 추가. 이 smoke test가 AGENTS.md의 미검증 전제(codex가 AGENTS.md를 자동 로드하는가)를 실제로 검증하는 단계다.
- **왜**: 기존 완료조건("템플릿 존재 + STATE 정확")은 협업 harness가 *실제로 작동하는지*를 검증하지 못한다. 문서만 맞고 codex가 규약을 안 따르면 관찰가능성·소유권이 무너진다. 연구 Phase A로 넘어가기 전 harness를 한 번 실증해야 안전하다.
- **대안**: smoke test 없이 바로 Phase A 진입 — 거부(미검증 harness 위에 연구를 쌓는 위험). 단, smoke test의 **설계·발주는 별도 세션**에서 하기로 하여 이번 세션 범위는 넘기지 않음.

## 2026-06-21 — 산출물 위치 확정 + data/ git 비추적
- **무엇**: codex 산출물 위치를 `scripts/`(코드)·`outputs/`(결과물)·`data/`(데이터)로 확정. **`data/`는 git에 추적하지 않음(.gitignore 대상)**, 대용량 정책(LFS 등)은 Phase A 데이터 반입 전 별도 결정.
- **왜**: 템플릿이 이미 outputs/·scripts/를 암시해 그에 맞춤. 데이터는 용량이 커 git에 넣으면 저장소가 망가지므로 추적 제외가 합리적 기본.
- **대안**: data/도 git 추적 — 거부(대용량 저장소 오염). 위치 미정으로 비워둠 — 거부(codex가 막힘).

## 2026-06-21 — 커밋 메시지 표준형 `docs:` 로 통일
- **무엇**: 커밋 메시지 표준을 `<type>: <요약>`(콜론 뒤 공백 한 칸)로 확정. 앞으로의 커밋만 이 형식으로 통일한다.
- **왜**: 기존 커밋은 `docs : `(콜론 양옆 공백) 구형식이었는데, 이는 git에 익숙치 않아 생긴 형태. Conventional Commits 등 일반 git 관례와 맞추는 게 도구 호환·가독성에 낫다.
- **정직성**: 과거 커밋 메시지는 위조·rewrite 하지 않는다. 통일은 향후 커밋에만 적용. conventions.md §4 각주에 과거가 구형식이었음을 명시.
- **대안**: 구형식 `docs : ` 유지 — 거부(비표준). 과거 커밋 rewrite — 거부(히스토리 위조).

## 2026-06-22 — constraints.md 확정 + hard 전환은 smoke test 이후로 보류
- **무엇**: constraints.md를 집행 장부로 확정. 강제 메커니즘 8행을 환경 점검값(적용됨 1 / 가능하나 미설정 1 / 미확인 2 / soft 4)으로 정직하게 기록. hard 후보 우선순위(1.codex docs 수정금지 2.git push 사람전용 3.report 의무)와 수단 메뉴를 적되 **지금 hard 전환은 하지 않음**.
- **왜**: codex를 아직 한 번도 안 돌려봤다. 실제로 뚫리는 규칙을 smoke test에서 본 뒤 거기부터 hard화해야 낭비가 없다. soft를 hard인 척 적는 것이 가장 위험한 rot라, 상태 용어(soft/가능하나 미설정/적용됨/미확인)를 정의해 능력과 약속을 구별.
- **대안**: 지금 전면 hard화 — 거부(미검증 상태에서 비용만, 정작 안 뚫리는 곳 막을 위험). 전부 soft로 뭉뚱그림 — 거부(적용됨/미확인을 soft로 왜곡 = 거짓 안심).

## 2026-06-22 — AGENTS.md §7 ↔ constraints.md 불일치 3건 발견, 갱신은 다음 라운드
- **무엇**: 이번 환경 점검으로 AGENTS.md §7 강제상태 표가 constraints.md와 불일치함을 발견. 3건: (1) §7 "쓰기 경계 = soft"인데 실제 codex docs 수정금지 집행은 **미확인**(soft 아님, 미확인≠soft) — 과장. (2) git commit/push 행에 push측 branch protection "가능하나 미설정" 누락. (3) 실제 적용 중인 `.gitignore data/`(적용됨) 누락.
- **왜 지금 안 고치나**: **한 세션에 두 문서를 동시에 수정하면 어느 쪽이 기준인지 흐려진다.** 이번 세션의 기준 문서는 constraints.md다. AGENTS.md는 다음 라운드에서 constraints를 기준으로 갱신한다.
- **언제**: 다음 라운드(권장: smoke test 설계 세션과 함께 또는 그 직전). STATE.md 열린 항목에 등록.

## 2026-06-22 — SPEC-001 smoke test 합격 판정 (harness 작동 확인)
- **무엇을 검증했나**: REPORT-001을 SPEC-001 §5 완료조건 7항목과 1:1 대조 + 사람 관찰 반영. harness 4가지(AGENTS 자동부팅 / 쓰기경계 / report 의무 / conventions)가 추적 흔적으로 확인되는지로 판정.
- **합격 판정 + 근거**:
  - 검증① **AGENTS 자동로드 = YES**. codex가 constraints/conventions/SPEC-001만 읽고 부팅 — AGENTS §2 "딱 셋만"이 실제 작동. **AGENTS.md의 '미검증 전제'(codex가 AGENTS.md를 자동 로드하는가)가 이로써 검증됨(1회).**
  - 검증② **쓰기 경계 = YES**. codex 변경은 scripts/·outputs/·reports/·sessions.md 4곳뿐. constitution/plan/state/specs/decisions 0 변경.
  - 검증③④ **report 의무·conventions = YES**. REPORT-001은 _TEMPLATE 형식, sessions.md codex 1줄 append, 파일명·위치·결과 1행 모두 규약대로.
- **'M docs/tasks/SMOKE_TEST_OBSERVE.md'의 정체 (해명)**: 이 변경은 codex가 아니라 **사람(JUN)이 관찰 메모의 체크박스를 채우며 생긴 것**이다. codex는 그 파일을 수정·되돌리지 않고 §5-4를 `[ ]`로 두며 report에 정직하게 신고했다. 따라서 경계 위반이 아니라 **멈춤·정직성 규칙의 정상 동작**이며, codex의 "부분완료" 상태표기는 과대주장 회피의 모범 사례로 평가한다.
- **대안**: §5-4를 형식상 미충족으로 보아 '불합격/재발주' — 거부. 미충족 원인이 codex 책임이 아니고 harness 4가지는 모두 충족되었으므로, 형식 실패로 합격을 뒤집는 것은 검증의 본래 목적(harness 작동 확인)에 어긋난다.

## 2026-06-22 — Phase 0 졸업 + Phase A 전환
- **무엇**: smoke test 합격으로 Phase 0(Scaffold) 완료조건 5개 전부 충족 → **Phase 0 졸업**. current_phase.md를 Phase A(Onboarding)로 전환. Phase A 완료조건 = A.1 reading / A.2 도구학습 / A.3 dataset target list 확정, 엄격한 게이트는 A.3.
- **A.3 완료조건은 '가볍게 시작 → 진행하며 구체화'**: 1차 충족은 cell line 이름 목록(3–5 + 후보 5–10). list를 만들다 완료조건이 자라나면(예: 이름만으론 Phase B에서 못 쓴다 → GEO accession·ecDNA 근거 항목 추가) **그때마다 decisions.md에 한 줄** 남긴다. (지금 과하게 정의하지 않는다 — results-driven.)
- **왜**: 미리 완료조건을 무겁게 박으면 추측이 된다. 학습/큐레이션 phase는 진행하며 무엇이 필요한지 드러난다. A.3=사람작업 결정은 유지(2026-06-21).

## 2026-06-22 — constraints.md·AGENTS.md §7 강제상태 동기화 (smoke test 반영 + 불일치 3건 해소)
- **무엇**: smoke test 결과를 두 문서에 정직하게 반영. (a) constraints: codex docs수정금지·sandbox경계 행을 '미확인' → 'soft(1회 확인)'로(자기규율 1회 작동, hard는 미적용). hard 전환 로드맵에 "soft가 1회 작동했으므로 당장 hard화 보류" 명시. (b) AGENTS §7: 밀려있던 불일치 3건 해소 — 쓰기경계 soft→'soft(1회확인)/hard미적용', push/branch-protection 행 추가, .gitignore data/(적용됨) 반영. 두 표 일관 동기화.
- **왜**: 점검으로 알아낸 것을 표에 반영하지 않으면 rot. 단 "1회 관찰 ≠ 영구 보장"·"여전히 hard 없음"을 명시해 과장 금지. 한 세션에 두 문서를 섞지 말라는 원칙대로 [3]→[4] 순차 진행.
- **대안**: 'soft 규율 1회 작동'을 '검증됨/안전'으로 적기 — 거부(과장 = 거짓 안심 rot). 지금 hard화 강행 — 거부(1회 작동했고 뚫린 적 없어 비용 낭비).
