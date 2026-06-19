<!--
last-updated: <YYYY-MM-DD>
session-id: <YYYY-MM-DD-꼬리표>
author-agent: cowork
-->

# SPEC-<번호> — <짧은 제목>

> cowork가 codex에게 발주하는 작업 지시서. codex는 AGENTS.md + 이 spec만 읽고 일한다.
> 채팅 맥락을 모른다고 가정하고 **자기완결적으로** 쓴다.

| 항목 | 값 |
|---|---|
| spec-id | SPEC-<번호> |
| 발주일 | <YYYY-MM-DD> |
| 발주자 | cowork |
| 연결 phase | <plan/current_phase.md 의 어느 단계> |
| 우선순위 | <상/중/하> |
| 짝 report | REPORT-<같은 번호> (codex가 작성) |

## 1. 무엇을 (What)
<한 문장으로 산출 목표. 모호하지 않게.>

## 2. 왜 (Why)
<이 작업이 어느 질문/phase에 기여하는지. 근거 docs 경로를 링크.>
- 근거: `docs/...`

## 3. 입력 (Inputs)
<데이터·파일·이전 산출물의 정확한 경로/출처. 없으면 "없음".>

## 4. 산출물 (Outputs)
<생성될 파일과 위치를 구체적으로. 예: `outputs/embedding_umap.png`, `scripts/run_embed.py`>

## 5. 완료조건 (Done = 검증 가능하게) ⚠️ 가장 중요
<cowork가 다음 세션에 yes/no로 대조할 수 있는 체크리스트. 모호하면 검증 불가 = 관찰가능성 실패.>
- [ ] <예: `outputs/embedding_umap.png` 가 생성됨>
- [ ] <예: README에 재현 명령(1줄)이 있음>
- [ ] <예: report에 사용한 입력 데이터 버전·shape가 기록됨>

## 6. 건드리지 말 것 (Out of scope / Do-not-touch)
<수정 금지 영역. 쓰기 경계(constraints.md) 위반 방지.>
- `docs/constitution/`, `docs/plan/`, `docs/state/` — 수정 금지 (cowork 소유)
- <기타 손대면 안 되는 코드/데이터>

## 7. 위험·승인 필요 (해당 시)
<영구 삭제·권한 변경·외부 공유 등 위험 작업이면 사람 승인 필요. 없으면 "없음".>
