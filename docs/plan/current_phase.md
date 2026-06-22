<!--
last-updated: 2026-06-22
session-id: 2026-06-22-constraints
author-agent: cowork
-->

# current_phase.md — 지금 phase 목표 + 완료조건

## 현재 phase: Phase 0 — Scaffold (부팅 골격 구축)
연구 Phase A 진입 전, 협업 인프라(docs 골격 + spec↔report 계약 + codex 진입점)를
세우는 단계. **우리는 지금 Phase 0의 졸업 직전이다.**

### 걸어온 길 (히스토리 — 판정 도구 아님)
> 완료 *판정*은 아래 "Phase 0 완료조건" 체크리스트가 단일 진실이다. 이 블록은
> 무슨 일이 언제 있었는지의 서술일 뿐, 여기엔 체크박스를 두지 않는다.

- 2026-06-03 — docs/ 골격 생성, spec/report 템플릿 합의 (`d55b6d1`).
- 2026-06-21 — AGENTS.md 작성·합의·커밋 (`a9817a4`).
- 2026-06-21 — 도구1이 `knowledge/ecDNA_FM_guide.md` 투입 (`4bb28f7`).
- 2026-06-21 — plan(roadmap/current_phase) 실내용 작성·사람 합의 완료.
- 2026-06-22 — constitution 3종(roles·conventions·constraints) 실내용 작성·합의 완료.

### Phase 0 완료조건 (졸업 판정의 단일 진실 — 체크박스는 여기에만)
- [x] docs 골격 + spec/report 템플릿 합의·존재.
- [x] AGENTS.md 작성·합의·커밋.
- [x] plan(roadmap/current_phase) 실내용 합의 (2026-06-21).
- [x] constitution 실내용 합의 — roles·conventions·constraints 3종 완료 (2026-06-22).
- [ ] **harness smoke test 통과**: 시험용 spec 1건을 codex에 발주하여, codex가
      AGENTS.md 부팅·쓰기경계·report 의무를 실제로 따르는지 `tasks/reports/`의 report와
      `log/sessions.md` 흔적으로 확인한다. 이는 AGENTS.md에 박힌 **미검증 전제
      — "codex가 AGENTS.md를 자동 로드하는가"** 를 검증하는 단계다. 결과는
      `log/decisions.md`에 기록한다.
      - **순서 의존**: smoke test는 **constraints.md(constitution)가 실내용으로 채워진
        뒤에** 한다. 빈 constitution으로는 codex가 지킬 경계가 없어 검증 대상이 없기
        때문이다. (즉 위 'constitution 실내용 합의' 항목이 이 항목의 선행조건.)
      - ※ 이 smoke test의 **설계·발주는 이번 세션이 아니라 별도 세션**에서 한다.

### Phase 0 → Phase A 전환조건
위 완료조건 다섯 항목이 **전부 [x]** 가 되면 Phase 0 졸업, Phase A로 전환한다.
**남은 관문은 'harness smoke test 통과' 하나뿐이다** (constitution까지 완료됨).

---

## 다음 phase 미리보기: Phase A — Onboarding
> 상세는 `docs/plan/roadmap.md`의 Phase A 칸과 `docs/knowledge/ecDNA_FM_guide.md` 참조.

- **Phase A 완료조건** = dataset **target list 확정** (가이드 A.3): 우선 cell line 3–5개
  + 후보 5–10개.
- **단, A.3은 codex spec이 아니라 사람(+도구1) 작업이다.** 이유: AmpliconRepository.org
  academic email 등록(계정 인증은 사람 몫)과, 어느 cell line을 우선할지의 판단이 섞인
  큐레이션이라 자동화 대상이 아니다. (이 결정은 `log/decisions.md` 2026-06-21 참조.)
