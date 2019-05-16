INCLUDE Irvine32.inc
; Reversing a String (RevStr.asm)
; This program reverses a string.
.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword
.data
	inp DWORD 0 ;store the number of inputs
.code
main proc
	call ReadInt  ;read int
	mov inp , eax	;move number of inputs to inp
	mov ecx , inp	;move number of inputs to ecx register
L1:				
	Call ReadInt	;read int
	push eax		;push to stack
	loop L1

	mov ecx , inp	;move again to ecx
L2:
	pop eax		;pop top value to eax
	call WriteInt	; print to screen
	call crlf	;change line
	loop L2
	
	Invoke ExitProcess,0
	main endp
end main