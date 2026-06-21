<!--
last-updated: 2026-06-21
session-id: 2026-06-21-agents-md
author-agent: cowork
-->

# STATE.md — 살아있는 단일 스냅샷

> 이 파일은 "지금 어디"의 단일 진실이다. 매 세션 종료 시 현재 진실로 **덮어쓴다**.

## 지금 phase
**Phase 0 — Scaffold** (연구 Phase A 진입 전, 협업 인프라 구축 중)

## 방금 한 것 (2026-06-21-agents-md)
- AGENTS.md(도구3 codex 부팅 진입점) 초안 작성 → 사람 합의로 확정. 저장소 루트에 위치.
- 설계 원칙 "좁게 가두기": codex는 spec 하나만 읽고(constraints·conventions·그 spec), 경계 안에만 쓰고, report로 추적, 막히면 멈춤.
- 정합성 (A)(B) 대조 통과: reports 템플릿 의무 ↔ AGENTS §4·§5 / specs §7 ↔ AGENTS §5.
- "codex가 AGENTS.md를 자동 로드한다"는 가정을 **미검증 전제**로 문서에 명시 (실검증은 사람이 codex-GUI에서 추후).

## 다음 할 것
- (다음 세션) constitution / plan **실내용 채우기** (현재 PLACEHOLDER), Phase A 목표·완료조건 정의.
- (대기) 도구1(사람)의 `docs/knowledge/` 학습 입력 — Phase A 방향과 AGENTS §6 포인터의 실질 전제.
- (사람) codex-GUI에서 AGENTS.md 자동 로드 여부 검증 → 결과를 decisions.md에 기록.
- (향후) 쓰기 경계의 환경 강제 메커니즘(read-only 마운트 / branch 보호 / sandbox) 설계.

## 미해결 질문
- codex-GUI가 AGENTS.md를 실제로 자동 로드하는가 (미검증 전제).
- 모든 soft 경계를 언제 환경 강제로 승격할지.
- docs/knowledge/ 가 비어 있어 Phase A 방향을 아직 못 정함 — 사람의 학습 입력 대기.
