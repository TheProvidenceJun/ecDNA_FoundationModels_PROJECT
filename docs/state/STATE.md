<!--
last-updated: 2026-06-22
session-id: 2026-06-22-spec-001-smoke-test
author-agent: cowork
-->

# STATE.md — 살아있는 단일 스냅샷

> 이 파일은 "지금 어디"의 단일 진실이다. 매 세션 종료 시 현재 진실로 **덮어쓴다**.

## 지금 phase
**Phase 0 — Scaffold** (졸업 직전. constitution 완성됨. **남은 관문은 harness smoke test 하나**).

## 방금 한 것 (2026-06-22-spec-001-smoke-test)
- harness smoke test용 첫 spec 작성·합의: `tasks/specs/SPEC-001-smoke-test.md` (_TEMPLATE 형식, 자기완결적, ecDNA/Phase 언급 없음).
  - codex에게 줄 더미 작업: `scripts/smoke_test.py`(표준라이브러리, 4줄 출력) + `outputs/smoke_test_result.txt`. 함정 없음.
  - 완료조건은 codex 자가체크 + cowork yes/no 대조 가능한 체크리스트. §6에 "docs/ 전체 수정 금지(reports·sessions append만 예외)" 명시. §7 위험 없음.
- 사람용 구동·관찰 메모 작성: `tasks/SMOKE_TEST_OBSERVE.md` (codex에 주지 않음. AGENTS 자동로드 흔적·git diff·report/sessions 흔적 점검 + 합격기준).

## 다음 할 것
- (사람/JUN) **codex-GUI에서 SPEC-001 발주·구동** → `SMOKE_TEST_OBSERVE.md` 절차로 관찰 → 결과(git status, REPORT-001, sessions 줄, AGENTS 자동로드 여부)를 cowork에 전달.
- (cowork, 다음 세션) REPORT-001을 SPEC-001 §5와 **대조 검증** → 결과를 `decisions.md`에 기록. 통과 시 Phase 0 완료조건 'harness smoke test 통과' [x] → **Phase 0 졸업 → Phase A 전환**.
- (다음 라운드) **AGENTS.md §7 강제상태 표 갱신** — constraints.md 기준 불일치 3건 해소(열린 항목). smoke test 결과(미확인 2건)도 함께 반영 가능.
- (사람/도구1, 병행 가능) Phase A.3 dataset 매핑.
- (Phase A 데이터 반입 전) data/ 대용량 정책(LFS 등) 결정.

## 미해결 질문 / 열린 항목
- **AGENTS.md §7 강제상태 표 갱신 필요** — constraints.md 점검 결과와 불일치 3건: (1) 쓰기경계 soft→미확인, (2) push/branch-protection 행 추가, (3) `.gitignore data/` 반영. 다음 라운드에서 처리. (근거: decisions.md 2026-06-22.)
- GitHub branch protection 실제 설정 여부 (현재 '가능하나 미설정') — smoke test 전후.
- codex sandbox / read-only 마운트 (현재 '미확인') — smoke test에서 codex 실제 행동으로 확인.
- codex-GUI가 AGENTS.md를 자동 로드하는가 (미검증 전제) — smoke test로 검증.

## Phase 0 완료조건 현황 (판정 단일 진실은 current_phase.md)
- [x] docs 골격 + 템플릿 / [x] AGENTS.md / [x] plan 실내용 합의 / [x] constitution 실내용 합의
- [ ] harness smoke test 통과 ← **마지막 관문. SPEC-001 발주됨, codex 구동·검증 대기.**
