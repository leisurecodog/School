INCLUDE Irvine32.inc
; Reversing a String (RevStr.asm)
; This program reverses a string.
.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword
.data
	str1 BYTE "X",0 ;printed by following code
	Temp DWORD ?	;Being used to store L1 loop counter
.code
main proc
	mov ecx , 16	;initial counter for L1
	mov ebx , 0		;use to show color
	mov edx , offset str1	;move the address of str1 to edx
L1:
	mov Temp , ecx  ;store L1 counter
	mov ecx , 16	;assign L2 counter value
L2:
	mov eax ,ebx	;move the color value to eax(ebx)
	inc ebx			;increase ebx to show next color
	call SetTextColor
	call WriteString	
	loop L2
	call crlf	
	mov ecx , Temp	;back the value of L1 counter
	loop L1
	mov eax,15 ; set color to initial color
	call SetTextColor
	Invoke ExitProcess,0
	main endp
end main