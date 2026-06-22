<!--
last-updated: 2026-06-22
session-id: 2026-06-22-verify-graduate
author-agent: cowork
-->

# STATE.md — 살아있는 단일 스냅샷

> 이 파일은 "지금 어디"의 단일 진실이다. 매 세션 종료 시 현재 진실로 **덮어쓴다**.

## 지금 phase
**Phase A — Onboarding** (배경·도구 학습 + dataset 확정). **Phase 0(Scaffold)은 2026-06-22 졸업.**

## 방금 한 것 (2026-06-22-verify-graduate)
- **REPORT-001 ↔ SPEC-001 §5 대조 검증 → 합격.** harness 4가지(AGENTS 자동부팅·쓰기경계·report·conventions) 추적 흔적으로 확인. AGENTS '미검증 전제'(자동 로드) 검증됨(1회). `M SMOKE_TEST_OBSERVE.md`는 사람 관찰 체크 흔적이며 codex가 정직 신고 → 정상 동작. (decisions.md 기록.)
- **Phase 0 졸업 + current_phase.md를 Phase A로 전환**(사람 합의). A.3 완료조건은 '가볍게 시작 → 진행하며 구체화'.
- **constraints.md 갱신**: codex docs수정금지·sandbox 경계 '미확인'→'soft(1회 확인)', hard화 보류 명시.
- **AGENTS.md §7 정정**: 밀려있던 불일치 3건 해소, constraints와 동기화 완료.

## 다음 할 것
- (사람/도구1) **Phase A 착수**: A.1 reading, A.2 도구 학습(scanpy·scFM·inferCNV), **A.3 dataset target list** 작성(핵심 게이트, 사람 작업). 진행 중 A.3 완료조건이 자라나면 decisions.md에 한 줄.
- (cowork) Phase A 중 codex 발주가 필요한 코드 작업(예: scanpy/embedding 프로토타입)이 생기면 그때 spec으로 분리.
- (향후) GitHub branch protection 설정 여부, codex 경계 hard화는 '뚫리는 사례' 나올 때.
- (Phase A 데이터 반입 전) data/ 대용량 정책(LFS 등) 결정.

## 미해결 질문 / 열린 항목
- (해소됨) ~~AGENTS §7 불일치 3건~~ → 2026-06-22 동기화 완료.
- (해소됨, 1회) ~~codex AGENTS 자동 로드 미검증 전제~~ → smoke test로 검증(1회 관찰, 영구 보장 아님).
- branch protection 실제 설정 (현재 '가능하나 미설정').
- codex 경계 준수는 '1회 관찰'이지 영구 보장 아님 — 추가 작업에서 계속 관찰.

## Phase A 완료조건 현황 (판정 단일 진실은 current_phase.md)
- [ ] A.1 reading / [ ] A.2 도구 학습 / [ ] A.3 dataset target list 확정 ← 핵심 게이트
