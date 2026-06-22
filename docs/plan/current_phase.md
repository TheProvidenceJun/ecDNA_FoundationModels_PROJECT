<!--
last-updated: 2026-06-22
session-id: 2026-06-22-verify-graduate
author-agent: cowork
-->

# current_phase.md — 지금 phase 목표 + 완료조건

## 현재 phase: Phase A — Onboarding (배경·도구 학습 + dataset 확정)
> 상세는 `docs/plan/roadmap.md` Phase A 칸 + `docs/knowledge/ecDNA_FM_guide.md` (A.1~A.3).

**Phase 0(Scaffold)은 2026-06-22 졸업했다.** 협업 harness(docs 골격·spec↔report 계약·
codex 진입점·constitution)가 SPEC-001 smoke test로 1회 실증되었다. 이제 연구의 첫 단계인
Phase A로 들어간다.

### 걸어온 길 (히스토리 — 판정 도구 아님)
- 2026-06-03 ~ 06-22 — Phase 0 Scaffold: docs 골격·템플릿·AGENTS.md·plan·constitution 구축.
- 2026-06-22 — **SPEC-001 smoke test 합격** → harness 4가지(AGENTS 자동부팅·쓰기경계·report·conventions) 실증. **Phase 0 졸업.** (검증 근거: `log/decisions.md` 2026-06-22.)

### Phase A 목표
프로젝트에 필요한 **배경 지식·도구를 익히고, 사용할 dataset target list를 확정**한다.
(이 phase의 산출물 무게중심은 A.3 dataset 매핑이다.)

### Phase A 완료조건 (졸업 판정의 단일 진실 — 체크박스는 여기에만)
- [ ] **A.1 필수 reading** — ecDNA biology(Wu 2019, Hung 2021, Lange 2022) + scFM(Geneformer, scGPT) 핵심 읽기. 완료 신호 = 사람이 `knowledge/`에 정리 노트 투입(또는 구두 확인).
- [ ] **A.2 도구 학습** — scanpy(PBMC3K 전 과정), scFM API(Geneformer·scGPT embedding 추출), ground-truth pipeline(inferCNV/CopyKAT) 실습. 완료 신호 = 실습 흔적(노트/스크립트).
- [ ] **A.3 dataset target list 확정** ⚠️ 핵심 deliverable — **가볍게 시작한다**: 우선 cell line **3–5개 + 후보 5–10개**의 *이름 목록*을 명시한 문서가 저장소에 존재(`knowledge/` 또는 `plan/`)하면 1차 충족.
  - **진행하며 구체화한다.** list를 실제로 만들다 보면 완료조건 자체가 자라날 수 있다(예: "이름만으론 Phase B에서 못 쓴다 → GEO accession·ecDNA 근거·scRNA 가용성 항목 추가"). **완료조건을 강화·수정할 때마다 `log/decisions.md`에 한 줄**(무엇을·왜)을 남긴다.
  - **A.3은 codex가 아니라 사람(+도구1) 작업이다** (AmpliconRepository 계정 인증 + 판단 섞인 큐레이션이라 자동화 대상 아님 — `log/decisions.md` 2026-06-21).

> Phase A는 대부분 **사람/도구1의 학습·큐레이션**이다. codex 발주가 필요한 코드 작업
> (예: scanpy/embedding 프로토타입)이 생기면 그때 spec으로 분리한다 — 지금 미리 정하지 않는다.

### Phase A → Phase B 전환조건
**A.3 target list가 확정되어야** Phase B(Frozen scFM × carrier detection)에 착수한다.
dataset 매핑이 안 끝나면 B로 가지 않는다(carrier detection은 데이터가 전제).
A.1·A.2는 B 착수 전 충분히 진행되어야 하나, 엄격한 게이트는 A.3이다.

---

## 다음 phase 미리보기: Phase B — Frozen scFM × carrier detection
> 상세는 `docs/plan/roadmap.md` Phase B 칸.

- scFM이 zero-shot으로 ecDNA carrier cell을 transcriptome만으로 구분하는지 평가(frozen-first).
- 착수 전제 = Phase A의 dataset target list 확정.
