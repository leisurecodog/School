INCLUDE Irvine32.inc

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.data
CoLoR BYTE 15,15,15,9,10,10,10,10,10,10
Str1 BYTE "Show Text Color",0
.code


main proc
	mov ecx , 20	;loop times
	mov edx , offset Str1	;the string we want to show
L1:
	mov eax , 10	;range of random
	call RandomRange ;store a number between 0~9 in eax reg
	mov esi , eax	; move index pos
	movzx eax , CoLoR[esi]	;choose color
	call SetTextColor	;setcolor
	call WriteString	;show text
	call Crlf	;new line
	loop L1		
	mov eax , 15	;white color
	call SetTextColor   ; restore color
	exit
	main endp
end main