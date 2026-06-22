<!--
last-updated: 2026-06-21
session-id: 2026-06-21-constitution-roles-conventions
author-agent: cowork
-->

# STATE.md — 살아있는 단일 스냅샷

> 이 파일은 "지금 어디"의 단일 진실이다. 매 세션 종료 시 현재 진실로 **덮어쓴다**.

## 지금 phase
**Phase 0 — Scaffold** (졸업 직전. 남은 관문: constraints.md 채우기로 constitution 완성 → harness smoke test).

## 방금 한 것 (2026-06-21-constitution-roles-conventions)
- constitution 두 문서 실내용 작성·합의: `roles.md`, `conventions.md` (PLACEHOLDER 제거).
- `roles.md`: 도구1/2/3 권한 표 명문화. CLAUDE.md §4·AGENTS.md §3과 대조 → **충돌 없음** 확인.
- `conventions.md`: 헤더·파일명(SPEC/REPORT 3자리 0패딩 001~)·산출물위치·커밋규약·로그형식 명문화.
- 확정된 새 결정 3건 decisions.md 기록: 산출물 위치(data/는 git 비추적), 커밋 표준형 `docs:` 통일.
- **constraints.md는 이번에 건드리지 않음** (사람 결정 필요 — 다음 라운드 별도 처리).

## 다음 할 것
- (다음 라운드) **constraints.md 채우기** — 사람 결정 필요(강제 메커니즘 등). 끝나면 'constitution 실내용 합의' 완료조건 [x].
- (constitution 완성 후, 별도 세션) **harness smoke test 설계·발주** → 미검증 전제 해소.
- (사람/도구1, 병행 가능) Phase A.3 dataset 매핑.
- (Phase A 데이터 반입 전) data/ 대용량 정책(LFS 등) 결정 + `.gitignore`에 data/ 추가.

## 미해결 질문
- codex-GUI가 AGENTS.md를 실제로 자동 로드하는가 (smoke test로 검증 예정).
- soft 경계를 언제 환경 강제로 승격할지 (constraints.md에서 다룰 주제).

## Phase 0 완료조건 현황 (판정 단일 진실은 current_phase.md)
- [x] docs 골격 + 템플릿 / [x] AGENTS.md / [x] plan 실내용 합의
- [ ] constitution 실내용 합의 — roles·conventions 완료, **constraints.md 남음**
- [ ] harness smoke test 통과
