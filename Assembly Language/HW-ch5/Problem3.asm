INCLUDE Irvine32.inc
; Reversing a String (RevStr.asm)
; This program reverses a string.
.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.code
main proc
	call CMYSTRING
	Invoke ExitProcess,0
	main endp
end main