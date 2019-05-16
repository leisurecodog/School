INCLUDE Irvine32.inc
.386
.model flat,stdcall
.stack 4096
ExitProcess PROTO,dwExitCode:DWORD
;�{������:
;�]���C�Ӧr�굲���������@�ӪŦr���A�ҥH��������source���ڪ��Ŧr����target
;�M��source�r��q�Y�}�l�@�Ӥ@�ӽƻs��dl
;��dl�ƻs��target�Ŧr�����e�@�Ӧ�m�A�C�C���e�ƻs�A�ΰj��h�B�z
.data
source BYTE "This is the source string",0
target BYTE SIZEOF source DUP('#')
ttt BYTE ?
.code
main PROC
	mov edx , offset target 
	mov eax , offset source			; eax as a pointer to string source
	mov ebx , offset target			; ebx as a pointer to string target
	mov ecx , SIZEOF source	-1		; the L1 counter is size of string source
	add ebx , SIZEOF source -1		; move ebx pointer to bottom of string target
	add eax , SIZEOF source -1		; move eax pointer to bottom of string source
	mov dl , BYTE PTR [eax]			; move the null char of string source to dl
	mov BYTE PTR [ebx] , dl			; move dl to last position of string target
	sub eax , SIZEOF source-1		; back the eax pointer to first position
	dec ebx							; officially start reversing string

L1:
	mov dl , BYTE PTR [eax]			; move the string source char to dl
	mov BYTE PTR [ebx] , dl			; move dl to string target
	inc eax							; add eax , 1
	dec ebx							; sub ebx , 1
loop L1
	mov edx , offset target 
	call WriteString
INVOKE ExitProcess,0
main ENDP
END main