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
