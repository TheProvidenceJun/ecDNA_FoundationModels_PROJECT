<!--
last-updated: 2026-06-22
session-id: 2026-06-22-constraints
author-agent: cowork
-->

# STATE.md — 살아있는 단일 스냅샷

> 이 파일은 "지금 어디"의 단일 진실이다. 매 세션 종료 시 현재 진실로 **덮어쓴다**.

## 지금 phase
**Phase 0 — Scaffold** (졸업 직전. constitution 완성됨. **남은 관문은 harness smoke test 하나**).

## 방금 한 것 (2026-06-22-constraints)
- constitution 마지막 문서 `constraints.md` 작성·합의 → **constitution 3종 완성**.
- 집행 장부 성격으로 작성: 강제 메커니즘 8행을 환경 점검값으로 정직하게(적용됨 1·가능하나 미설정 1·미확인 2·soft 4). 상태 용어 정의(soft≠미확인). hard 전환은 smoke test 이후로 보류, 후보 우선순위·수단 메뉴만 기록.
- AGENTS.md §7 ↔ constraints 불일치 3건 발견 → **AGENTS.md는 건드리지 않고** 열린 항목으로 등록(아래).
- decisions.md 2건 기록, current_phase.md의 'constitution 합의' [x] 갱신.

## 다음 할 것
- (다음 라운드) **AGENTS.md §7 강제상태 표 갱신** — constraints.md 기준으로 불일치 3건 해소(아래 열린 항목).
- (그 후/함께, 별도 세션) **harness smoke test 설계·발주** — Phase 0의 마지막 관문. codex 실제 행동으로 미확인 2건(codex docs 수정금지 집행, sandbox 경계) + 미검증 전제(AGENTS 자동 로드) 점검.
- (사람/도구1, 병행 가능) Phase A.3 dataset 매핑.
- (Phase A 데이터 반입 전) data/ 대용량 정책(LFS 등) 결정.

## 미해결 질문 / 열린 항목
- **AGENTS.md §7 강제상태 표 갱신 필요** — constraints.md 점검 결과와 불일치 3건: (1) 쓰기경계 soft→미확인, (2) push/branch-protection 행 추가, (3) `.gitignore data/` 반영. 다음 라운드에서 처리. (근거: decisions.md 2026-06-22.)
- GitHub branch protection 실제 설정 여부 (현재 '가능하나 미설정') — smoke test 전후.
- codex sandbox / read-only 마운트 (현재 '미확인') — smoke test에서 codex 실제 행동으로 확인.
- codex-GUI가 AGENTS.md를 자동 로드하는가 (미검증 전제) — smoke test로 검증.

## Phase 0 완료조건 현황 (판정 단일 진실은 current_phase.md)
- [x] docs 골격 + 템플릿 / [x] AGENTS.md / [x] plan 실내용 합의 / [x] constitution 실내용 합의
- [ ] harness smoke test 통과 ← **마지막 남은 관문**
