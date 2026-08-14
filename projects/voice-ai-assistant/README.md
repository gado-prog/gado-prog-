# 🎙️ Voice AI Assistant

Low-latency voice assistant architecture combining speech recognition, reasoning and speech synthesis behind an API.

## Flow

`Audio → ASR → Intent/Agent → Tools → Response → TTS → Audio`

## Engineering focus

- Streaming-friendly API boundaries
- Conversation state
- Tool permissions
- Latency measurement
- Provider-agnostic adapters

## Stack

Python · FastAPI · ASR · TTS · WebSocket/SSE
