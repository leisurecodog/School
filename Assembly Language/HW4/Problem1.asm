INCLUDE Irvine32.inc
.386
.model flat,stdcall
.stack 4096
ExitProcess PROTO,dwExitCode:DWORD

.data
arrayD DWORD 1,2,3,4
str1 BYTE "Before be exchanged:",0
str2 BYTE "After be exchanged:",0
str3 BYTE " ",0
A DWORD ?
B DWORD ?
.code
main PROC
	mov edx , offset str1	;move address of str1 to edx
	call WriteString		;call str1
	mov edx , offset str3	;move address of str3 to edx
	;----------move arrayD[1~4] to eax and show----------
	mov eax , arrayD
	call WriteDec
	call WriteString
	mov eax , arrayD+4
	call WriteDec
	call WriteString
	mov eax , arrayD+8
	call WriteDec
	call WriteString
	mov eax , arrayD+12
	call WriteDec
	call WriteString
	call Crlf
	;----------exchange segment----------
	mov eax , arrayD+8		;eax=3
	mov A , eax				;A=3
	mov eax , arrayD+12		;eax=4
	mov B , eax				;B=4
	mov eax , arrayD		;eax=1
	mov arrayD+12 , eax		;arrayD[4]=1
	mov eax , arrayD+4		;eax=2
	mov arrayD+8 , eax		;arrayD[3]=2
	mov eax , A				;eax=3
	mov arrayD , eax		;arrayD[1]
	mov eax , B				;eax=4
	mov arrayD+4 , eax		; arrayD[2]=4

	mov edx , offset str2	;move address of str2 to edx
	call WriteString		;call str1
	mov edx , offset str3	;move address of str3 to edx
	;----------move arrayD[1~4] to eax and show----------
	mov eax , arrayD
	call WriteDec
	call WriteString
	mov eax , arrayD+4
	call WriteDec
	call WriteString
	mov eax , arrayD+8
	call WriteDec
	call WriteString
	mov eax , arrayD+12
	call WriteDec
	call WriteString
	call Crlf
INVOKE ExitProcess,0
main ENDP
END main